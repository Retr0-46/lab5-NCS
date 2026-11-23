# Task 3 summary: the DAST report

Lab 5 DevSecOps | Task 3 | 23 November 2026

This is the ZAP report that the `dast_scan` job produced. The raw files are in this folder. The run that produced them is [CI run 45147326709](https://github.com/KroJIak/lab5-NCS/actions/runs/45147326709), on commit `7b32679`. The scanner was ZAP 2.17.0.

## How the scan was set up

The job starts the official PyGoat container as a service and points ZAP at it.

```yaml
services:
  pygoat:
    image: pygoat/pygoat:latest
    ports:
      - 8000:8000
```

ZAP then runs a baseline scan against the running application.

```yaml
- name: ZAP Baseline Scan
  uses: zaproxy/action-baseline@v0.15.0
  with:
    target: 'http://localhost:8000'
    cmd_options: '-a -j'
    allow_issue_writing: false
    artifact_name: zap-scan-report
```

The `-a` flag adds the alpha passive scan rules and `-j` uses the modern spider next to the traditional one.

## Three problems we had to fix

**The readiness step waited for the wrong code.** It looked for HTTP 200, but PyGoat answers `/` with a 302 redirect to the login page, so the check could never pass. The step ran out of retries and exited 1, and the ZAP step was skipped every time. The check now accepts any status below 500, and it prints what it got.

```
PyGoat is up (HTTP 302)
```

**The DAST job could have been skipped when the Bandit job failed.** The Bandit job fails on purpose, because it finds real problems. A job that depends on it is skipped when one of its dependencies fails, so without `if: always()` the dynamic scan would never have run either. The DAST job now has `needs` together with `if: always()`.

**The action could not upload its own artifact.** The action version the job used, v0.12.0, uploads the report with an old version of the artifacts library. Its own upload step failed with `Create Artifact Container failed: The artifact name zap_scan is not valid`, even though the name itself was fine. The separate `Upload ZAP Report` step in the workflow was not affected, so the report was not lost. The action was upgraded to v0.15.0, and now both uploads work.

## What the scan found

ZAP reported 23 alerts on the pages of the main PyGoat application. The counts below come from the JSON report in this folder.

| Risk level | Alerts |
|---|---|
| High | 0 |
| Medium | 3 |
| Low | 9 |
| Informational | 11 |

The three Medium alerts are the ones worth reading first.

**Content Security Policy (CSP) Header Not Set, rule 10038.** Five pages are served without a `Content-Security-Policy` header. Without this header the browser does not know which scripts and which sources are allowed, so any script that gets into a page can do more than it should.

**Source Code Disclosure - Python, rule 10099.** One response contained Python source code. A debug page or a stack trace returned the contents of a source file. It gives an attacker the layout of the application for free.

**Absence of Anti-CSRF Tokens, rule 10202.** Four forms change state without a token that ties them to the session. A logged in user who visits a crafted page can be made to send a request without knowing it.

The Low and Informational alerts are listed here with the number of instances of each.

| Alert | Rule | Instances |
|---|---|---|
| Full Path Disclosure | 110009 | 13 |
| Base64 Disclosure | 10094 | 12 |
| Session Management Response Identified | 10112 | 11 |
| User Controllable HTML Element Attribute (Potential XSS) | 10031 | 8 |
| Content Security Policy Header Not Set | 10038 | 5 |
| Server Leaks Version Information via "Server" HTTP Response Header Field | 10036 | 5 |
| Cookie No HttpOnly Flag | 10010 | 5 |
| Permissions Policy Header Not Set | 10063 | 5 |
| Non-Storable Content | 10049 | 5 |
| Modern Web Application | 10109 | 5 |
| Cross-Origin-Embedder-Policy Header Missing or Invalid | 90004 | 5 |
| Cross-Origin-Resource-Policy Header Missing or Invalid | 90004 | 5 |
| X-Content-Type-Options Header Missing | 10021 | 4 |
| Absence of Anti-CSRF Tokens | 10202 | 4 |
| Private IP Disclosure | 2 | 4 |
| Application Error Disclosure | 90022 | 4 |
| Authentication Request Identified | 10111 | 2 |
| Sec-Fetch-Dest Header is Missing | 90005 | 3 |
| Sec-Fetch-Mode Header is Missing | 90005 | 3 |
| Sec-Fetch-Site Header is Missing | 90005 | 3 |
| Sec-Fetch-User Header is Missing | 90005 | 3 |
| Storable and Cacheable Content | 10049 | 1 |
| Source Code Disclosure - Python | 10099 | 1 |

The job log puts the same result as 18 warnings and 53 passes, with 0 failures.

## Reading the results

Most of the rest is low risk housekeeping. Missing security headers such as `Content-Security-Policy`, `Permissions-Policy` and `X-Content-Type-Options` show up on every page. Full Path Disclosure means the error pages show the path of the Python packages on the server. Base64 Disclosure is not a problem in itself, the application uses base64 for the CSRF tokens of the application, but it does mean the tokens are not encrypted.

Rule 10031 deserves a second look even though ZAP rates it Informational. The application copies the value of the `login` field into the `value` attribute of an `<input>` tag on the login and signup pages, without encoding it. That is the shape of a cross site scripting bug. The low rating comes from the passive rule, not from a test of the exploit.

The scan has limits worth keeping in mind. ZAP ran without a login, so it only saw the pages that are open to a visitor. The report shows the login, signup and password reset pages, the static files, and the two challenge shortcuts `/ba` and `/sql`. Those two answer with a 302 redirect to the login, so no lab was actually reached. The rules were run at the default level plus the alpha passive rules, so a more complete pass would use a full scan with an authenticated context file.

## Why the job is green now

The `DAST with OWASP ZAP` job is green in the newest runs, and the report is uploaded twice, as `zap-scan-report` and as `zap-dast-report`.

Two different things were red before, and only one of them was about the findings.

The `ZAP Baseline Scan` step was red because the action could not upload its own artifact. That was the bug in the old action version, and the fix was to upgrade it.

The Bandit job is still red, and that one is on purpose. Bandit returns a non-zero exit code when it finds something, and it finds 52 problems in this repository. A green Bandit job would mean the scanner stopped working.

The DAST job does not go red for the findings, because the action has a `fail_action` input and it is false by default. The alerts are in the report and in the job summary, they just do not change the status of the step.
