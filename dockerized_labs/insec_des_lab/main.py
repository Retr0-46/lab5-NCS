from flask import Flask, render_template, request
import base64
import hashlib
import hmac
import json
import os
from dataclasses import dataclass

app = Flask(__name__)

# Key used to sign the tokens handed to the browser.
# It stays on the server, so a user cannot produce a valid token on their own.
# It has to be set through the environment, because a key that ships with the
# source code is a public key.
SECRET_KEY = os.environ.get("INSEC_DES_SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError(
        "INSEC_DES_SECRET_KEY is not set. The signing key must not be part of "
        "the source code, so the lab refuses to start without it."
    )

ALLOWED_FIELDS = ("username", "is_admin")


@dataclass
class User:
    username: str
    is_admin: bool = False


def sign(payload: str) -> str:
    """Return the HMAC-SHA256 signature of the given text."""
    return hmac.new(SECRET_KEY.encode(), payload.encode(), hashlib.sha256).hexdigest()


def serialize_user(user: User) -> str:
    """Turn a user into a signed token that only this server can produce."""
    body = json.dumps(
        {"username": user.username, "is_admin": user.is_admin}, sort_keys=True
    )
    envelope = json.dumps({"data": body, "signature": sign(body)}, sort_keys=True)
    return base64.b64encode(envelope.encode()).decode()


def deserialize_user(token: str) -> User:
    """
    Turn a token back into a user.

    The signature is checked first, so a token that was edited by the user is
    rejected before any value is used.
    """
    envelope = json.loads(base64.b64decode(token).decode())
    body = envelope["data"]
    signature = envelope["signature"]

    if not hmac.compare_digest(sign(body), signature):
        raise ValueError("Invalid token signature")

    data = json.loads(body)
    if not isinstance(data, dict):
        raise ValueError("Unexpected token format")

    data = {key: value for key, value in data.items() if key in ALLOWED_FIELDS}

    username = data.get("username", "")
    is_admin = data.get("is_admin", False)
    if not isinstance(username, str) or not isinstance(is_admin, bool):
        raise ValueError("Unexpected token format")

    return User(username=username, is_admin=is_admin)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/serialize", methods=["POST"])
def serialize_data():
    username = request.form.get("username", "guest")
    user = User(username=username, is_admin=False)
    serialized = serialize_user(user)
    return render_template("result.html", serialized=serialized)


@app.route("/deserialize", methods=["POST"])
def deserialize_data():
    try:
        token = request.form.get("serialized_data", "")
        user = deserialize_user(token)

        if user.is_admin:
            message = f"Welcome Admin {user.username}! Here's the secret admin content: ADMIN_KEY_123"
        else:
            message = f"Welcome {user.username}. Only admins can see the secret content."

        return render_template("result.html", message=message)
    except Exception as e:
        return render_template("result.html", message=f"Error: {str(e)}")


@app.route("/health")
def health_check():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
