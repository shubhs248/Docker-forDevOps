# Exercise 2.1 — Containerize the App

**You write:** a clean, basic `Dockerfile` for the Flask app in `../app/`.

---

## 📋 The spec
Write a `Dockerfile` that:

- starts from a small, **pinned** Python base image (`python:3.12-slim`)
- sets the working directory to `/app`
- copies `app/requirements.txt` **first** and installs the dependencies
  (so this layer is cached until the requirements change)
- then copies the rest of the app code from `app/`
- sets an environment variable `APP_ENV=production`
- documents the port with `EXPOSE 5000`
- starts the app with `python app.py`

## ✅ How to check
```bash
docker build -f my-Dockerfile -t lab-app:1 .
docker run --rm -p 5000:5000 lab-app:1
curl http://localhost:5000          # JSON greeting, environment = production
curl http://localhost:5000/health   # {"status":"ok"}
```
Compare with [`solutions/Dockerfile.exercise-1`](solutions/Dockerfile.exercise-1).

## 💡 Hints
- Order matters for caching: copy `requirements.txt` and `pip install` **before** copying the code.
- Use `pip install --no-cache-dir` to avoid storing the pip cache in the image.
- The container listens on port 5000 because `app.py` runs `app.run(host="0.0.0.0", port=5000)`.
- Build from the **repo root** (the `.` at the end) so Docker can see the `app/` folder.
