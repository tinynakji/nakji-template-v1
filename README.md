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
Stack:
* AWS EKS
 - In VPC, with an EC2 machine to interact from
* RDS in VPC
* AWS Load Balancer in VPC
* Certificate Manager
* Domain Name Management

Main IAM Role with the following permissions:
- TODO

And Trusted Relations
```
TODO
```

Steps:


### Only restart UI or web
```
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