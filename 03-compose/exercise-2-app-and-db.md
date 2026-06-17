# Exercise 3.2 — App + Database

**You write:** a `compose.yaml` with the app **and** a Postgres database that keeps its data.

---

## 📋 The spec
Write a Compose file with two services and a volume:

- **web**:
  - builds from `.`
  - maps port `5000:5000`
  - environment: `APP_ENV=production` and `DATABASE_URL=postgresql://app:secret@db:5432/appdb`
    (note the host is `db` — the other service's name!)
  - `depends_on` the `db` service
- **db**:
  - image `postgres:16`
  - environment: `POSTGRES_USER=app`, `POSTGRES_PASSWORD=secret`, `POSTGRES_DB=appdb`
  - stores its data in a **named volume** `db-data` mounted at `/var/lib/postgresql/data`
- a top-level `volumes:` section declaring `db-data`

## ✅ How to check
```bash
docker compose -f my-compose.yaml up --build
curl http://localhost:5000          # database_url is now set
docker compose -f my-compose.yaml down      # data survives in the volume
```
Compare with [`solutions/exercise-2-app-and-db.yaml`](solutions/exercise-2-app-and-db.yaml).

## 💡 Hints
- Services reach each other by **service name**: the app connects to `db`, not `localhost`.
- A named volume keeps the database data even after `docker compose down` (use `down -v` to delete it).
- The top-level `volumes:` just lists the name: `db-data:` (empty value).
