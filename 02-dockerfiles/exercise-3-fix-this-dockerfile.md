# Exercise 2.3 — Fix This Dockerfile

**You fix:** the bad habits in [`broken.Dockerfile`](broken.Dockerfile).

---

## 📋 The situation
`broken.Dockerfile` builds, but it is large, slow to rebuild, and runs as root. Here it is:

```dockerfile
FROM python
ADD . /app
WORKDIR /app
RUN pip install flask
RUN pip install gunicorn
RUN apt-get update
RUN apt-get install -y curl
CMD python app/app.py
```

## 🎯 Your task
Rewrite it so it follows good practice. Fix at least these problems:

| Problem in the file | Why it's bad | The fix |
|---------------------|--------------|---------|
| `FROM python` | untagged = huge & unpredictable | pin a slim tag, e.g. `python:3.12-slim` |
| `ADD . /app` | `ADD` has surprising behaviour; copies everything | use `COPY`, and add a `.dockerignore` |
| installing packages by hand | not reproducible | `COPY app/requirements.txt` then `pip install -r` |
| two separate `pip install` + later code copy | breaks layer caching | copy requirements first, install, then copy code |
| `apt-get update` and `install` in separate `RUN`s | stale cache, bigger image | combine, add `--no-install-recommends`, clean `apt` lists |
| runs as root | security risk | add and switch to a non-root user |
| no `EXPOSE` | undocumented port | add `EXPOSE 5000` |
| `CMD python ...` (shell form) | no clean signal handling | use exec form: `CMD ["python", "app.py"]` |

Also create a **`.dockerignore`** so things like `.git` and `__pycache__` are not copied in.

## ✅ How to check
```bash
docker build -f my-fixed-Dockerfile -t lab-app:3 .
docker run --rm -p 5000:5000 lab-app:3
curl http://localhost:5000
docker image ls lab-app    # the fixed image should be much smaller than the broken one
```
Compare with [`solutions/Dockerfile.exercise-3-fixed`](solutions/Dockerfile.exercise-3-fixed)
and [`solutions/.dockerignore`](solutions/.dockerignore).
