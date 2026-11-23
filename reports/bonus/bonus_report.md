# Bonus task: fixing the unsafe pickle deserialization

Lab 5 DevSecOps   |   Bonus task   |   23 November 2026

I patched the B301 finding that I described in my Task 4 report. The change is in the application code, not in a dependency version.

Repository: [Retr0-46/lab5-NCS](https://github.com/Retr0-46/lab5-NCS)   |   Vulnerable commit: `54d165f`   |   Fix commits: `ad465c5` for the code, `7aad5a2` for the key handling and the tests

Files changed: dockerized_labs/insec_des_lab/main.py, dockerized_labs/insec_des_lab/test_app.py, dockerized_labs/insec_des_lab/entrypoint.sh, dockerized_labs/insec_des_lab/Dockerfile

## What was wrong

The lab serialized a user object with `pickle.dumps()` and read it back with `pickle.loads()`. The token came from a form field, so anybody could send their own bytes to the server. Pickle treats those bytes as a list of instructions, so a crafted token made the server run commands. My Task 4 report has the full analysis.

## The fix

Pickle is gone from the handler. The token is now a JSON document with an HMAC-SHA256 signature, and the server keeps the signing key to itself.

```python
def serialize_user(user: User) -> str:
    body = json.dumps(
        {"username": user.username, "is_admin": user.is_admin}, sort_keys=True
    )
    envelope = json.dumps({"data": body, "signature": sign(body)}, sort_keys=True)
    return base64.b64encode(envelope.encode()).decode()


def deserialize_user(token: str) -> User:
    envelope = json.loads(base64.b64decode(token).decode())
    body = envelope["data"]
    signature = envelope["signature"]

    if not hmac.compare_digest(sign(body), signature):
        raise ValueError("Invalid token signature")

    data = json.loads(body)
    ...
```

Three things stop an attacker here.

The signature is checked before any value is used. A user who edits the token changes the JSON body, so the signature no longer matches and the request is rejected. The comparison uses `hmac.compare_digest`, which does not leak how much of the signature was correct.

JSON has no way to call a function. Even a valid JSON document can only carry strings, numbers, lists and objects, so the "run this code" ability of pickle is gone for good.

The fields are filtered through an allowlist and type checked, so only `username` and `is_admin` are read and both have to have the expected type.

The signing key is the fourth piece. It is read from the `INSEC_DES_SECRET_KEY` environment variable and the lab refuses to start without it, because a key that sits in the source code is a public key. The container generates a random one on each start when the variable is not set, so the key never leaves the container.

## Before and after

The Bandit scan of the whole repository with the same flags as our CI job gives the following.

| | B301 findings | Total findings | Medium | High |
|---|---|---|---|---|
| Before the patch | 2 | 53 | 30 | 23 |
| After the patch | 1 | 52 | 29 | 23 |

The finding in dockerized_labs/insec_des_lab/main.py is gone. The one in dockerized_labs/software_integrity_lab/app.py is still there because it is a different lab and a different code path, and it was not part of my patch.

The raw numbers are in [bandit-before-after.txt](bandit-before-after.txt) and the Bandit text report after the patch is [bandit-b301-after.txt](bandit-b301-after.txt). The `bandit-findings` artifact of the CI run below gives the same numbers, 52 findings with 29 Medium, 23 High and one B301.

## Running the app after the fix

I ran the patched lab locally with Python 3.13.5, Flask 3.0.0 and Werkzeug 3.0.1, on loopback at port 8080.

The normal path still works. I created a user and sent the token back, and the app said "Welcome guest. Only admins can see the secret content."

![Normal user token accepted after the fix.](images/fixed-normal-user.png)

*Figure 1. The regular flow still works.*

The attack from my Task 4 report now fails. I took the token, changed `is_admin` to true in the JSON body and sent it back.

![Result page showing the rejected forged token.](images/fixed-forged-admin-rejected.png)

*Figure 2. The forged admin token is rejected with "Invalid token signature".*

The pickle payload also fails. The old attack sent a base64 encoded pickle that ran `id` on the server.

![Before the fix, the id command output appeared in the response.](images/before-rce-command-output.png)

*Figure 3. Before the patch, the server ran the command and showed its output.*

After the patch the same payload produces a decode error and nothing is executed. I also checked that the file the payload wanted to create was not created, inside the container as well as on my machine.

I added four tests in dockerized_labs/insec_des_lab/test_app.py. They cover the normal flow, the attempt to change the admin flag and two pickle payloads.

```bash
python -m unittest dockerized_labs.insec_des_lab.test_app -v
```

```
test_admin_flag_cannot_be_changed ... ok
test_normal_user_can_be_deserialized ... ok
test_pickle_payload_does_not_run_code ... ok
test_pickle_payload_output_is_not_shown ... ok

Ran 4 tests in 0.012s

OK
```

I checked that the two payload tests really do catch the old code. I ran them against the vulnerable version from commit `54d165f` and there the payload wrote its marker file and the `id` output appeared in the response. On the patched code neither happens.

## Why the Bandit and image scan jobs still fail

The Bandit job in our pipeline still ends with a red mark, and that is expected. My patch removes one finding out of 53. The other 52 stay because they are separate problems in other labs: the app still runs Flask with debug turned on, still binds to all interfaces, still uses weak hashes and still has an `eval()` call in the command injection lab. A red Bandit job is the correct signal for this pipeline. It means the scanner is doing its job.

The Docker Scout job fails before Scout even starts. The repository secrets `DOCKERHUB_USERNAME` and `DOCKERHUB_PASSWORD` are not set, so the step that logs in to Docker Hub cannot run and both Scout steps are skipped. Scout needs a Docker Hub account to check, and a free one is enough, but somebody with admin rights on the repository has to add those secrets first. Because the job stops there, this run produced no CVE data at all, so nothing can be said about the base image from it.

The DAST job stays green. The ZAP action has a `fail_action` input and it is false by default, so the alerts show up in the report and in the job summary without failing the step. The job log lists 18 warnings in 18 rule groups, mostly missing security headers on the pages of the main PyGoat application, which is a different application from the lab I patched. Fixing those headers on every page of the whole app is a much bigger job than this one.

## Pipeline run

The scan that proves the fix is here: [CI run 45153049583](https://github.com/KroJIak/lab5-NCS/actions/runs/45153049583). It runs on a commit that carries the whole patch, and the `bandit-findings` artifact of that run holds the numbers above.

The Bandit job in that run ends with a red mark, which is the expected result. The DAST job produced a ZAP report again, and the report from the first successful run is in [reports/dast](../dast/README.md).

## References

- [MITRE CWE-502](https://cwe.mitre.org/data/definitions/502.html)
- [Bandit B301 documentation](https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle)
- [OWASP Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)
- [My Task 4 report on this finding](../task4/pickle_deserialization_report.md)
