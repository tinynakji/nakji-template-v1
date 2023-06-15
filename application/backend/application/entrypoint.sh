#!/bin/sh
# gunicorn --chdir --bind 0.0.0.0:5000 wsgi:app
# ( cd /usr/src/app/flask_app ; alembic upgrade head )
gunicorn --bind 0.0.0.0:5000 wsgi:app
