# 🤝 Contributing

Thanks for thinking about helping out! This is a learning project, so contributions of every size are welcome — even fixing a typo.

If this repo helped you, the easiest way to support it is to **star** ⭐ it, **fork** 🍴 it, and **share** 🔗 it on LinkedIn so others can find it too.

## Ways you can help

- **Fix something** — a typo, a broken link, or a Dockerfile/Compose file that does not work.
- **Add a new exercise** — another Dockerfile pattern, a new Compose stack, or a bigger sample app.
- **Improve the wording** — make an explanation clearer or simpler.
- **Add another language sample** — a Node or Go app to containerize would be great.

## How to contribute (step by step)

1. **Fork** this repo to your own GitHub account.
2. **Clone** your fork:
   ```bash
   git clone https://github.com/<your-username>/docker-practice-lab.git
   cd docker-practice-lab
   ```
3. **Create a branch**:
   ```bash
   git switch -c add-node-sample
   ```
4. **Make your change** and test it (see the checklist below).
5. **Commit** and **push**, then open a **Pull Request**:
   ```bash
   git add .
   git commit -m "Add a Node.js sample app to containerize"
   git push -u origin add-node-sample
   ```

## Adding an exercise

Keep the same simple style:

- For Part 2: add an `exercise-*.md` brief and a working `Dockerfile.*` in `solutions/`.
- For Part 3: add an `exercise-*.md` brief and a working `*.yaml` Compose file in `solutions/`.
- Use plain, simple English.

## Checklist before you open a PR

- [ ] Dockerfiles build: `docker build -f <file> -t test .`
- [ ] Compose files start: `docker compose -f <file> up --build` (and `docker compose -f <file> config` is clean).
- [ ] Images follow the best-practice checklist in the cheatsheet (pinned base, non-root, `.dockerignore`, etc.).
- [ ] Instructions use plain, simple English.
- [ ] If you added a new part, you linked it from the main `README.md`.

## Code of conduct

Be kind and helpful. Assume good intent and keep feedback friendly.

---

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
