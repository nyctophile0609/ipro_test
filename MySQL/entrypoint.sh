#!/bin/sh
while ! mysqladmin ping -h"mysql" --silent; do
    echo "Waiting for MySQL..."
    sleep 2
done


if python3 database/create_super_user.py; then
    echo "Super user created successfully."
else
    echo "Failed to create super user."
    exit 1  # Exit with error code if the script fails
fi

exec "$@"
