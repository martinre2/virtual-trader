# virtual-trader
NASDAQ virtual trading environment

### Prerequisites

If you want to run the project on Docker, first you should have some applications installed:

```bash
docker
docker-compose
Poetry
dbmate
```

```bash
pip install docker-compose
```

```bash
pip install poetry
```

---

## Run

### Docker

1. Start the application

```bash
make up
```

2. Stop the application
```bash
make down
```

### Hostnames for accessing the service directly

* Local: http://127.0.0.1:8000/docs#

Use the credentials:

User: `johndoe`
Password: `password`

or

User: `alice`
Password: `password`

> the project provided a static users only for demonstrational purposes, this implementation is not production ready and is based on fastapi documentation [example](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/).

### Local environment

1. Access your virtual environment:

```bash
poetry shell
```

2. Install the project dependencies:

```bash
poetry install
```

3. Don't forget to run the [migrations](#migrations) and start the project:

```bash
uvicorn app.main:app --reload
```

---

## Running the tests

### Local environment

```bash
pytest -v /tests
```

## <a name="migrations"></a> Migrations

We use [DbMate](https://github.com/amacneil/dbmate), Refer to DBMate's documentation for any doubts on usage.

### Install dbmate

```bash
brew install dbmate
```

### Run migrations

to run all pending migrations type

```bash
dbmate up
```

---

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast, web framework for building APIs with Python 3.9+
- [PostgreSQL](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database
- [DbMate](https://github.com/amacneil/dbmate) - A lightweight, framework-agnostic database migration tool.
- [yfinance](https://github.com/ranaroussi/yfinance) - Download market data from Yahoo! Finance's API

---
