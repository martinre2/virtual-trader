#!/bin/bash
set -xe

workers=3

run_app() {
    exec uvicorn app.main:app --workers $workers --host 0.0.0.0 --http h11 --port 8000
}

dbmate -e "DATABASE_URL" -d "./db/migrations" up
run_app
