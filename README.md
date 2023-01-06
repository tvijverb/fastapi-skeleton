# FastAPI Skeleton App

## Start skeleton app
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

# Database Migrations
create new migration
```bash
alembic revision --autogenerate
```

run all pending migrations
```bash
alembic upgrade head
```


## Features
- Connection to **PostgreSQL** database
- Connection to **Redis** database
- **Alembic** ready with good naming convention
- **Health** endpoint to check if database is healthy
- **Sentry integration** is available by enabling `SENTRY_ENABLED` in `.env` file (`SENTRY_DSN` is required, `SENTRY_ENVIRONMENT` is optional)
