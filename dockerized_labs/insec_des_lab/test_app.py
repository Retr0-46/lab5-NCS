import base64
import json
import os
import pickle
import tempfile
import unittest

os.environ.setdefault("INSEC_DES_SECRET_KEY", "test-key-for-the-unit-tests")

from dockerized_labs.insec_des_lab.main import app, serialize_user  # noqa: E402


class InsecureDeserializationTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_normal_user_can_be_deserialized(self):
        response = self.client.post(
            "/serialize", data={"username": "guest"}
        )
        self.assertEqual(response.status_code, 200)

        token = response.data.decode().split("Your serialized token: ")[1].split("<")[0]
        response = self.client.post("/deserialize", data={"serialized_data": token})

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome guest", response.data)

    def test_admin_flag_cannot_be_changed(self):
        token = serialize_user(type("U", (), {"username": "attacker", "is_admin": False})())

        body = json.loads(base64.b64decode(token).decode())
        body["data"] = json.dumps({"username": "attacker", "is_admin": True})
        forged = base64.b64encode(json.dumps(body).encode()).decode()

        response = self.client.post("/deserialize", data={"serialized_data": forged})

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Invalid token signature", response.data)

    def test_pickle_payload_does_not_run_code(self):
        marker = os.path.join(tempfile.gettempdir(), "insec_des_lab_payload_marker")

        class Payload:
            def __reduce__(self):
                return (
                    exec,
                    (f"open({marker!r}, 'w').write('executed')",),
                )

        if os.path.exists(marker):
            os.remove(marker)

        payload = base64.b64encode(pickle.dumps(Payload())).decode()

        response = self.client.post("/deserialize", data={"serialized_data": payload})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            os.path.exists(marker),
            "the payload ran on the server",
        )

    def test_pickle_payload_output_is_not_shown(self):
        class Payload:
            def __reduce__(self):
                return (
                    exec,
                    ("raise Exception(__import__('os').popen('id').read())",),
                )

        payload = base64.b64encode(pickle.dumps(Payload())).decode()

        response = self.client.post("/deserialize", data={"serialized_data": payload})

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"uid=", response.data)


if __name__ == "__main__":
    unittest.main()
