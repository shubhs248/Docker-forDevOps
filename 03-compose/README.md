# Part 3 — Docker Compose

## 🎯 Goal
Run more than one container together. You will build up from a single service to a full
stack with a database, a cache, healthchecks, and restart policies.

## 🧠 What you practise here
- `services`, `build` vs `image`, `ports`, `environment`
- `depends_on` and talking to another service by its name
- named `volumes` for data that must survive restarts
- `healthcheck`, `restart`, and `depends_on: condition: service_healthy`

> 📌 These Compose files build the app from a Dockerfile. Before running them, put a
> working `Dockerfile` at the **repo root** (copy your answer from Part 2, e.g.
> `cp 02-dockerfiles/solutions/Dockerfile.exercise-1 Dockerfile`). The solution files
> use `build: .`, which looks for `./Dockerfile`.

---

## 📝 The 3 exercises

| # | File | What you practise |
|---|------|-------------------|
| 1 | `exercise-1-single-service.md`        | one service, build + ports + env |
| 2 | `exercise-2-app-and-db.md`            | app + Postgres with a named volume |
| 3 | `exercise-3-healthcheck-and-cache.md` | healthchecks, a Redis cache, restart policy |

For each one, write your `compose.yaml`, then:

```bash
docker compose -f my-compose.yaml config       # validate the file
docker compose -f my-compose.yaml up --build    # start the stack
docker compose -f my-compose.yaml down -v       # stop and remove (and volumes)
```

Ready-made answers are in [`solutions/`](solutions).

🎉 Finished all three parts? You can now containerize an app and run a multi-service stack — the core of day-to-day Docker work. Go back to the [main README](../README.md) and share your fork on LinkedIn!

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to add an exercise or fix something? See [CONTRIBUTING.md](../CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
