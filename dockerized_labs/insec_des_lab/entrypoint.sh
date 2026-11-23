#!/bin/sh
# The signing key must not be part of the source code, so it is either taken
# from the environment or generated here for this run of the container.
if [ -z "$INSEC_DES_SECRET_KEY" ]; then
    INSEC_DES_SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
    export INSEC_DES_SECRET_KEY
fi

exec flask run --debug --port=8080
