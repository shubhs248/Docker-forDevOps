# 🐳 Docker for DevOps — Practice Lab

> A **clone-and-go** lab to refresh Docker and practise the things you do on the job: write good **Dockerfiles**, fix bad ones, and wire up multi-service stacks with **Docker Compose**. Comes with a small real app to containerize.

[![Made with Docker](https://img.shields.io/badge/Made%20with-Docker-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 🎯 Why this repo?

Copy-pasting a `Dockerfile` from Stack Overflow works until it doesn't — the image is 1.2 GB, the build is slow, and it runs as root. This lab teaches the real skills: writing small, fast, safe images and composing services together, using one tiny web app as the running example.

## 🗂️ What's inside

```
docker-practice-lab/
├── README.md                 ← you are here
├── CHEATSHEET.md             ← 1-page Docker + Compose reminder
├── CONTRIBUTING.md           ← how to add your own exercises
├── app/                      ← the sample web app you containerize
│   ├── app.py
│   └── requirements.txt
├── 01-docker-basics/         ← warm-up: run, ps, logs, exec, images, prune
│   └── README.md
├── 02-dockerfiles/           ← write, optimize, and fix Dockerfiles
│   ├── README.md
│   ├── exercise-1-containerize-the-app.md
│   ├── exercise-2-multi-stage.md
│   ├── exercise-3-fix-this-dockerfile.md
│   ├── broken.Dockerfile     ← the one you fix in exercise 3
│   └── solutions/
└── 03-compose/               ← write Docker Compose files
    ├── README.md
    ├── exercise-1-single-service.md
    ├── exercise-2-app-and-db.md
    ├── exercise-3-healthcheck-and-cache.md
    └── solutions/
```

## ✅ Requirements

- **Docker** (and the Compose plugin) — check with `docker --version` and `docker compose version`.
- That's it. The sample app's own dependencies are installed **inside** the image, not on your machine.

> No Docker yet? Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/macOS) or Docker Engine (Linux). You can still read the exercises and write the files without it.

## 🚀 Quick start

```bash
# 1. Get the code
git clone https://github.com/shubhs248/docker-practice-lab.git
cd docker-practice-lab

# 2. (Part 2) Build an image from a Dockerfile and run it
docker build -f 02-dockerfiles/solutions/Dockerfile.exercise-1 -t lab-app:1 .
docker run --rm -p 5000:5000 lab-app:1
# open http://localhost:5000

# 3. (Part 3) Bring up a whole stack
docker compose -f 03-compose/solutions/exercise-2-app-and-db.yaml up --build
```

## 🧭 Suggested path (about 90 minutes)

| # | Part | What you practise | Time |
|---|------|-------------------|------|
| 1 | [Docker Basics](01-docker-basics/README.md) | `run` `ps` `logs` `exec` `images` `build` `prune` | 25 min |
| 2 | [Dockerfiles](02-dockerfiles/README.md) | containerize, multi-stage, fix a bad Dockerfile | 35 min |
| 3 | [Compose](03-compose/README.md) | single service, app + database, healthchecks & cache | 30 min |

## 📝 How each part works

- **Part 1** is a refresher: read it, run the commands, check the answers at the bottom.
- **Part 2**: read the brief, write your `Dockerfile`, build it, then compare with `solutions/`.
- **Part 3**: read the spec, write your `compose.yaml`, run it, then compare with `solutions/`.

---

## 🎤 Prepping for an interview?

After you've done the build and compose exercises, open **[INTERVIEW-QUESTIONS.md](INTERVIEW-QUESTIONS.md)** — the Docker & Compose questions interviewers actually ask (layers, caching, volumes, healthchecks), in plain English with short answers you can say out loud.

---

## ⭐ Found this useful?

- **Star** ⭐ the repo so more people discover it.
- **Fork** 🍴 it and practise on your own copy.
- **Share** 🔗 it on LinkedIn and tag me — I would love to see your progress.
- **Contribute** 🤝 a new exercise or fix. See [CONTRIBUTING.md](CONTRIBUTING.md).

## 👋 About the author

Made with care by **Shubham Sharma**.

- GitHub: [github.com/shubhs248](https://github.com/shubhs248)
- LinkedIn: [linkedin.com/in/shubhs248](https://www.linkedin.com/in/shubhs248)

## 📜 License

MIT — free to use, fork, teach with, and share. A star ⭐ or a tag on LinkedIn is always appreciated!
