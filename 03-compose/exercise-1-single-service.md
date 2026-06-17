# Exercise 3.1 — A Single Service

**You write:** a `compose.yaml` that builds and runs the app.

---

## 📋 The spec
Write a Compose file with one service:

- service name `web`
- it **builds** from the Dockerfile in the current directory (`build: .`)
- maps host port `5000` to container port `5000`
- sets the environment variable `APP_ENV` to `production`

## ✅ How to check
```bash
# put a Dockerfile at the repo root first (from Part 2)
cp 02-dockerfiles/solutions/Dockerfile.exercise-1 Dockerfile

docker compose -f my-compose.yaml config      # should print the parsed config
docker compose -f my-compose.yaml up --build
curl http://localhost:5000                     # environment = production
```
Compare with [`solutions/exercise-1-single-service.yaml`](solutions/exercise-1-single-service.yaml).

## 💡 Hints
- The top-level key is `services:`.
- `ports` is a **list** of `"host:container"` strings — quote `"5000:5000"`.
- `environment` can be a map: `APP_ENV: production`.
