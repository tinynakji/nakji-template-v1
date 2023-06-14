#nakji_template_v0

## Local Development Setup
### Database

Install Postgres: (2023-02-11) https://chartio.com/resources/tutorials/how-to-start-postgresql-server-on-mac-os-x/

```
$ brew update
$ brew doctor
$ brew install postgres
```

Start Postgres

```
$ postgres -D /usr/local/var/postgres
```

Create local db
```
createdb local_db
```

### Backend
```
cd backend/app
```

Apply database migrations
```
cd application
alembic upgrade head
alembic current
```

Start Gunicorn with the Flask app
```
cd ..
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

### Frontend
```
cd frontend/react_app
```

Install packages and start (requires npm and yarn)
```
yarn install
yarn dev
```

Check deployment
```
yarn build && yarn start
```

## Deployment
Requires `env.local` file; ask for example

### Locally start all apps
Aliases
```
alias dcb="docker-compose -f docker-compose.dev.yml build"
alias dcup="docker-compose -f docker-compose.dev.yml up -d"
alias dcdown="docker-compose -f docker-compose.dev.yml down"
alias dcdownv="docker-compose -f docker-compose.dev.yml down -v"
```
Commands to build and run:
```
dcdevb
dedevup
```

NOTE: This creates a fresh postgres instance; if you'd rather connect to a local postgres table, edit env vars accordingly and remove db from docker-compose

### Deploy with SSL enabled
```
# In remote machine
ssh root@${instance_host}
```

Some aliases
```
# Interacting with DO
alias do_rsync="rsync -a ./ root@${instance_host}:/home/${user}/workspace/"

alias dcprodb="docker-compose -f docker-compose.prod.yml build"
alias dcprodup="docker-compose -f docker-compose.prod.yml up -d"
alias dcproddown="docker-compose -f docker-compose.prod.yml down"
alias dcproddownv="docker-compose -f docker-compose.prod.yml down -v"
```

#### Create from scratch
```
dcprodb
dcprodup
```

Create SSL pem file
```
docker-compose stop webserver

mkdir dhparam

sudo openssl dhparam -out ./dhparam/dhparam-2048.pem 2048

docker-compose up -d --force-recreate --no-deps webserver
```

#### Renewing certificate
(haven't tested this yet, will do so after first expiration. Otherwise just start from scratch)
```
# DRYRUN, check that certificat CAN be created
docker-compose -f docker-compose.prod.yml run certbot renew --dry-run && docker-compose -f docker-compose.prod.yml  kill -s SIGNUP webserver

# Actual renewal
docker-compose -f docker-compose.prod.yml run certbot renew && docker-compose -f docker-compose.prod.yml  kill -s SIGNUP webserver
```

### Only restart UI or web
```
docker-compose -f docker-compose.prod.yml up --detach --build web
docker-compose -f docker-compose.prod.yml up --detach --build ui
```

### Interacting with postgres instance
```
# Dependent on database configs
psql -d nakjidb -U tinynakji
```

Taking a snapshot in the instance
```
pg_dump nakjidb -U tinynakji > ./snapshot.sql
```