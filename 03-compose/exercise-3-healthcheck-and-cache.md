# Exercise 3.3 — Healthchecks, a Cache, and Restart Policies

**You write:** a production-style `compose.yaml` with healthchecks, a Redis cache, and restart policies.

---

## 📋 The spec
Extend the previous stack to three services:

- **web**:
  - builds from `.`, maps `5000:5000`, `APP_ENV=production`
  - `restart: unless-stopped`
  - only starts once the database is healthy: `depends_on` → `db` with `condition: service_healthy`
  - a `healthcheck` that calls `http://localhost:5000/health` every 30s (timeout 5s, 3 retries)
- **db** (`postgres:16`):
  - same env as before (`POSTGRES_USER/PASSWORD/DB`) and the `db-data` volume
  - `restart: unless-stopped`
  - a `healthcheck` using `pg_isready -U app` every 10s (timeout 5s, 5 retries)
- **cache** (`redis:7`):
  - `restart: unless-stopped`
- a top-level `volumes:` with `db-data`

## ✅ How to check
```bash
docker compose -f my-compose.yaml config        # valid?
docker compose -f my-compose.yaml up --build
docker compose -f my-compose.yaml ps            # see health status next to each service
```
Compare with [`solutions/exercise-3-healthcheck-and-cache.yaml`](solutions/exercise-3-healthcheck-and-cache.yaml).

## 💡 Hints
- A healthcheck is a map under a service:
  ```yaml
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U app"]
    interval: 10s
    timeout: 5s
    retries: 5
  ```
- To wait for health, `depends_on` must use the long form:
  ```yaml
  depends_on:
    db:
      condition: service_healthy
  ```
- For the web healthcheck, a no-extra-tools option is Python (already in the image):
  `["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"]`
