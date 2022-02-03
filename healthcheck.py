#!/usr/local/bin/python
import os
import httpx

PORT = os.environ.get('GUNICORN_PORT', 10000)
assert httpx.get(f'http://localhost:{PORT}').status_code == 200
