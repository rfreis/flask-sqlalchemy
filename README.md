# Flask with SQLAlchemy, Postgres and Redis

Tutorial using Flask with SQLAlchemy, Postgres and Redis from [Flask by Example – Setting up Postgres, SQLAlchemy, and Alembic](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/) from [Real Python](https://realpython.com).

This app counts the words' frequency of selected URL.

## Requirements

To make this run you must have installed:

* docker
* docker-compose

## Running application

```bash
make start-local
```

### First running

On first running it is important setup the database

```bash
make load-db
```

## Stopping application

```bash
make stop
```

## Local bash

```bash
make local-bash
```

## Logs

```bash
make logs
```

## Opening the Word Count

Word Count will be available at:

- `localhost:5000/`
