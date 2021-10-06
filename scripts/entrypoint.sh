#!/usr/bin/env bash
: "${FERNET_KEY:=${FERNET_KEY:=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")}}"

export FERNET_KEY
airflow initdb
airflow webserver