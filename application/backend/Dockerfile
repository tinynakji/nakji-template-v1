# pull official base image
FROM python:3.10.7-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /usr/src/app/
ENV HOME = /home

# Create user and group
RUN mkdir -p /home/app
RUN groupadd -r app && useradd --no-log-init -r -g app app

# set work directory
WORKDIR $APP_HOME

# get packages for build
# RUN apt-get update && apt-get install -y gcc musl-dev postgresql-dev
# RUN apt-get update && apt-get install -y — no-install-recommends gcc
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# install dependencies
RUN pip install --upgrade pip
# RUN pip install flake8
COPY ./application/requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY application $APP_HOME
RUN pip install -e .

# install the application in editable mode
RUN chmod +x /usr/src/app/entrypoint.sh
RUN chown -R app:app $APP_HOME
USER app

# Expose port 5000 for the Flask application to listen on
EXPOSE 5000

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]