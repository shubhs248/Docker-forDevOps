# Part 2 — Dockerfiles

## 🎯 Goal
Write images that are **small, fast to build, and safe** — and learn to spot the bad habits that make images huge and slow.

## 🧠 What you practise here
- A clean basic Dockerfile (layer caching, `EXPOSE`, `CMD`)
- **Multi-stage** builds to shrink the final image
- Fixing common Dockerfile anti-patterns
- Using a `.dockerignore`

All exercises containerize the small Flask app in [`../app/`](../app).

---

## 📝 The 3 exercises

| # | File | What you practise |
|---|------|-------------------|
| 1 | `exercise-1-containerize-the-app.md` | a clean basic Dockerfile |
| 2 | `exercise-2-multi-stage.md`          | a multi-stage build + non-root user |
| 3 | `exercise-3-fix-this-dockerfile.md`  | fixing a bad Dockerfile (`broken.Dockerfile`) |

For each one, write your `Dockerfile`, build it, and run it:

```bash
# build (run from the repo root so the build context includes app/)
docker build -f my-Dockerfile -t lab-app:1 .

# run
docker run --rm -p 5000:5000 lab-app:1
# open http://localhost:5000  and  http://localhost:5000/health
```

Ready-made answers are in [`solutions/`](solutions). Try first, then check.

➡️ Next: [Part 3 — Compose](../03-compose/README.md).

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to add an exercise or fix something? See [CONTRIBUTING.md](../CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
