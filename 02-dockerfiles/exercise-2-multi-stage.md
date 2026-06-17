# Exercise 2.2 — Multi-Stage Build

**You write:** a multi-stage `Dockerfile` that keeps the final image small and runs as a non-root user.

---

## 📋 The spec
A multi-stage build uses one stage to **prepare** things and a second, clean stage for the
**final** image — so build-only tools never ship to production.

Write a `Dockerfile` with two stages:

1. **builder** stage (`python:3.12-slim`):
   - copy `app/requirements.txt`
   - build the dependencies into wheel files: `pip wheel --wheel-dir /wheels -r requirements.txt`
2. **final** stage (`python:3.12-slim`):
   - copy the wheels from the builder stage
   - install from those wheels **without** going to the internet
   - copy the app code from `app/`
   - create and switch to a **non-root** user
   - `EXPOSE 5000`
   - start the app with **gunicorn**: `gunicorn --bind 0.0.0.0:5000 app:app`

## ✅ How to check
```bash
docker build -f my-Dockerfile -t lab-app:2 .
docker run --rm -p 5000:5000 lab-app:2
curl http://localhost:5000
docker image ls lab-app           # compare the size with exercise 1
```
Compare with [`solutions/Dockerfile.exercise-2`](solutions/Dockerfile.exercise-2).

## 💡 Hints
- Name a stage: `FROM python:3.12-slim AS builder`.
- Copy between stages: `COPY --from=builder /wheels /wheels`.
- Install offline from wheels: `pip install --no-index --find-links=/wheels -r requirements.txt`.
- Make a user: `RUN useradd --create-home appuser` then `USER appuser`.
- `gunicorn ... app:app` means "the variable `app` inside `app.py`".
