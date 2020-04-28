#!/bin/bash

pg_uri="postgres://postgres:postgres@$1:5432/shield"

export PG_ENV=$1

until pg_isready -h "$1" -p 5432 -d imdb -U postgres
do
    echo "Waiting for postgres at: $pg_uri"
    sleep 4;
done
echo "pg open"

gunicorn --bind $2:5000 app:app