# 📋 Docker + Compose Quick-Revision Cheatsheet

A one-page reminder of the Docker you use most. Use it with the exercises.

## Images & containers
```bash
docker pull nginx:1.27           # download an image
docker images                    # list local images
docker run --rm -p 8080:80 nginx # run (map host:container ports, remove on exit)
docker run -d --name web nginx   # run in background with a name
docker ps                        # running containers   (docker ps -a = all)
docker logs web                  # see a container's output  (-f to follow)
docker exec -it web sh           # open a shell inside a running container
docker stop web && docker rm web # stop and remove
docker rmi nginx:1.27            # remove an image
```

## Building images
```bash
docker build -t myapp:1.0 .                 # build from ./Dockerfile, tag it
docker build -f path/to/Dockerfile -t x .   # use a Dockerfile elsewhere
docker tag myapp:1.0 myapp:latest           # add another tag
docker push registry/myapp:1.0              # push to a registry
docker history myapp:1.0                     # see the layers (and their size)
```

## Cleaning up (free disk)
```bash
docker system df                 # how much space Docker uses
docker container prune           # remove stopped containers
docker image prune               # remove dangling images
docker system prune -a           # remove everything unused (careful!)
```

## Volumes & networks
```bash
docker volume create data
docker run -v data:/var/lib/postgresql/data postgres:16   # named volume
docker run -v "$PWD":/app node:20                          # bind-mount a folder
docker network create appnet
docker run --network appnet ...
```

## Dockerfile essentials
```dockerfile
FROM python:3.12-slim        # ALWAYS pin a small, specific base
WORKDIR /app                 # set the working directory
COPY requirements.txt .      # copy deps first so this layer caches
RUN pip install --no-cache-dir -r requirements.txt
COPY . .                     # then copy the rest of the code
EXPOSE 5000                  # document the port
USER appuser                 # don't run as root
CMD ["python", "app.py"]     # exec form (preferred over shell form)
```

### Best-practice checklist
- Pin the base image tag (`python:3.12-slim`, not `python`).
- Copy `requirements`/`package.json` **before** the code, so dependency layers cache.
- Combine related `RUN` steps and clean up in the same layer (`rm -rf /var/lib/apt/lists/*`).
- Add a `.dockerignore` so junk (`.git`, `__pycache__`, `node_modules`) is not copied.
- Use a non-root `USER`.
- Use **multi-stage** builds to keep the final image small.
- Prefer the JSON exec form for `CMD`/`ENTRYPOINT`.

## .dockerignore (example)
```
.git
__pycache__/
*.pyc
.venv/
node_modules/
*.md
```

## Compose essentials
```yaml
services:
  web:
    build: .                 # build from local Dockerfile (or use image:)
    ports:
      - "5000:5000"
    environment:
      APP_ENV: production
    depends_on:
      - db
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

```bash
docker compose up --build       # build + start everything (-d for background)
docker compose ps               # what's running
docker compose logs -f web      # follow one service's logs
docker compose exec web sh      # shell into a service
docker compose down             # stop & remove (add -v to also delete volumes)
docker compose config           # validate & print the merged config
```

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to improve it? See [CONTRIBUTING.md](CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
