# 🎤 Docker & Compose — Interview Questions

> Docker is one of the most-tested DevOps topics. Plain-English answers you can say out loud, covering containers, Dockerfiles, images, and Compose. Do the build/compose exercises first, then use this to **explain** what's happening under the hood.

**How to use this file:** cover the answers, read a question, answer out loud, then check. For Dockerfile questions, be ready to explain *layers and caching* — that's where seniors are separated from juniors.

---

## 🟢 Warm-up

**1. What's the difference between a container and a virtual machine?**
A VM virtualises the whole hardware and runs a full guest OS — heavy, slow to start. A container shares the host's kernel and only packages the app plus its dependencies — lightweight, starts in seconds. Containers = isolation without a full OS per app.

**2. What's the difference between an image and a container?**
An **image** is the read-only template (the recipe). A **container** is a running instance of an image (the cake). You can run many containers from one image.

**3. What does `docker run` actually do?**
It creates a container from an image and starts it. Under the hood it pulls the image if missing, creates a writable layer on top, sets up networking, and runs the container's command.

**4. Difference between `docker stop` and `docker kill`?**
`stop` sends SIGTERM and waits (graceful shutdown), then SIGKILL after a timeout. `kill` sends SIGKILL immediately (forceful). Prefer `stop` so the app can clean up.

**5. How do you get a shell inside a running container?**
```bash
docker exec -it <container> sh   # or bash
```
`-it` gives you an interactive terminal. Great for debugging.

---

## 🔵 Images, layers & Dockerfiles

**6. What is a Docker layer, and why does it matter?**
Each instruction in a Dockerfile (`FROM`, `RUN`, `COPY`...) creates a layer. Layers are **cached and reused**. If a layer hasn't changed, Docker reuses it — making rebuilds fast. Understanding this is key to writing efficient Dockerfiles.

**7. Why copy `requirements.txt` (or `package.json`) before the rest of the code?**
So the dependency-install layer is cached. Dependencies change rarely; code changes often. If you `COPY . .` first, any code change busts the cache and reinstalls everything. Copying deps first keeps installs cached. (This is the core of the "fix this Dockerfile" exercise.)

**8. `CMD` vs `ENTRYPOINT`?**
- `ENTRYPOINT` — the fixed command that always runs.
- `CMD` — the default arguments (or default command), easily overridden at `docker run`.
Common pattern: `ENTRYPOINT ["python"]` + `CMD ["app.py"]`. Use **exec form** (JSON array) so signals reach the process.

**9. `COPY` vs `ADD`?**
`COPY` just copies files — use it almost always. `ADD` also auto-extracts tar archives and can fetch URLs, which is surprising/risky. Rule: prefer `COPY` unless you specifically need ADD's extras.

**10. What is a multi-stage build and why use it?**
You use one stage to build (with compilers, dev deps) and copy only the final artifact into a small runtime stage. The result is a much smaller, more secure image with no build tooling. (That's the multi-stage exercise.)

**11. How do you make a Docker image smaller?**
Use a slim/alpine base, multi-stage builds, combine `RUN` steps and clean up in the same layer (`rm -rf /var/lib/apt/lists/*`), add a `.dockerignore`, and don't install dev/build tools in the final image.

**12. What does `.dockerignore` do?**
It tells the build to skip files (`.git`, `node_modules`, `__pycache__`) so they aren't sent to the build or copied into the image. Keeps builds fast and images clean — and avoids leaking secrets.

**13. Why pin a base image tag (`python:3.12-slim` not `python`)?**
`latest`/untagged means your build can silently change when the base updates, breaking reproducibility. Pinning a specific version makes builds deterministic. For full reproducibility, pin by digest.

---

## 🟣 Networking, storage & runtime

**14. How do containers talk to each other?**
On the same Docker network, containers reach each other by **container/service name** as a hostname. Docker provides DNS. In Compose, services on the default network can use each other's service names directly.

**15. What's the difference between a volume and a bind mount?**
- **Volume** — Docker-managed storage (`docker volume create`), best for persistent data like databases.
- **Bind mount** — maps a host folder into the container, best for local development (live code).
Both keep data alive beyond the container's life.

**16. Why is data lost when a container is removed, and how do you keep it?**
A container's writable layer is deleted with the container. Persist data by writing it to a **volume** or bind mount that lives independently. (That's the app+db volume exercise.)

**17. What does port mapping (`-p 8080:80`) mean?**
`host:container`. It maps port 8080 on your machine to port 80 inside the container. Without it, the container's ports aren't reachable from outside.

**18. What is `EXPOSE` — does it publish a port?**
No. `EXPOSE` is **documentation** of which port the app listens on. You still need `-p` (or Compose `ports:`) to actually publish it. A common gotcha.

---

## 🟠 Docker Compose

**19. What problem does Docker Compose solve?**
It defines and runs **multi-container** apps from one `docker-compose.yml` — services, networks, volumes, env, dependencies — with one command (`docker compose up`). No long `docker run` commands to remember.

**20. What does `depends_on` do — and not do?**
It controls **start order**, but by default does *not* wait for the dependency to be **ready** (just started). To wait for readiness, add a `healthcheck` and `depends_on: condition: service_healthy`. (That's the healthcheck exercise.)

**21. What is a healthcheck and why use it?**
A command Docker runs periodically to test if a container is actually working (e.g. `curl localhost/health`). Orchestrators use it to restart unhealthy containers and to gate dependent services.

**22. How do you persist a database in Compose?**
Define a named volume and mount it at the DB's data directory:
```yaml
volumes:
  db-data:
services:
  db:
    image: postgres:16
    volumes:
      - db-data:/var/lib/postgresql/data
```

**23. What do the `restart` policies mean?**
`no` (default), `always` (always restart), `on-failure` (only on non-zero exit), `unless-stopped` (restart unless you manually stopped it). Used for resilience.

---

## 🔴 "Senior" / real-world

**24. Why shouldn't a container run as root?**
If the app is compromised, root in the container is a bigger risk (especially with mounts/escapes). Create and switch to a non-root `USER` in the Dockerfile to limit blast radius.

**25. A container starts then immediately exits. How do you debug it?**
Check `docker logs <container>`, confirm the main process stays in the foreground (containers stop when PID 1 exits), check the `CMD`/`ENTRYPOINT`, and run it interactively (`docker run -it ... sh`) to poke around. A background/daemonised process is a common cause.

**26. How do you handle secrets in Docker?**
Don't bake them into images or Dockerfiles (they persist in layers/history). Use runtime env vars from a secret store, Docker/Swarm secrets, or the orchestrator's secret mechanism (Kubernetes Secrets). Add secret files to `.dockerignore`.

**27. What's the difference between Docker and Kubernetes?**
Docker builds and runs containers on a host. Kubernetes **orchestrates** containers across many hosts — scheduling, scaling, self-healing, networking, rollouts. They're complementary: build with Docker, run at scale with Kubernetes.

**28. Your image is huge. Walk me through trimming it.**
Switch to a slim/alpine base, add multi-stage builds to drop build tools, combine and clean `RUN` layers, add `.dockerignore`, remove caches (`--no-cache-dir` for pip), and check `docker history` to see which layers are biggest.

**29. How do you scan an image for vulnerabilities?**
Tools like `docker scout`, Trivy, or Grype scan layers/packages for known CVEs. Integrate scanning into CI so vulnerable images don't ship. Keep base images updated.

---

## 🧠 Whiteboard / live prompts

Try these in this lab.

1. **Write a Dockerfile** to containerise a Python/Flask app (with caching done right).
2. **Convert it to a multi-stage build** and shrink the image.
3. **Fix a broken Dockerfile** (bad layer order, root user, unpinned base).
4. **Write a Compose file** for an app + Postgres with a persistent volume.
5. **Add a healthcheck** so the app waits for the DB to be ready.

---

## ⭐ Found this useful?
If this helped your prep, please **star** ⭐, **fork** 🍴, and **share** 🔗 the repo on LinkedIn. Got a Docker question from a real interview? Add it via [CONTRIBUTING.md](CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
