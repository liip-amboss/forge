#!/bin/bash
# We need to use bash because of the use of the /dev/tcp device

if [ ! -e "$VIRTUAL_ENV/bin" ]; then
    echo "Creating virtualenv at \"$VIRTUAL_ENV\""
    python -m venv "$VIRTUAL_ENV"
fi

if [ "$INITIAL" = "1" ]; then
    pip install -r requirements/dev.txt
fi

exec "${@}"
