
# Apex Arc Engine – GitHub & Docker Deployment Guide

This single guide explains **exactly how to package, push, and run** the Apex Arc Engine system using GitHub and Docker.

---

## 1. PROJECT STRUCTURE (Local Directory)

Create this folder structure locally:

```
apex-arc-engine/
├── Dockerfile
├── .env.template
├── README.md
├── requirements.txt
├── run_apex_daily.py
├── auto_narrative_generator.py
├── apex_simulator2.py
├── version.py
├── endpoints.py
├── __init__.py
├── data/
│   ├── Top_25_HR_Projections__Full_Apex_Stack_.csv
│   └── mlb_rosters_2025.csv
└── output/  ← generated daily
```

---

## 2. SETUP: requirements.txt

Create `requirements.txt`:

```
pandas
requests
```

(If you use email/SMTP: add `smtplib` — standard in Python 3.)

---

## 3. SETUP: .env.template

Create `.env.template` (rename to `.env` when deploying):

```
USE_DISCORD=false
DISCORD_WEBHOOK_URL=

USE_EMAIL=false
SMTP_SERVER=
SMTP_PORT=587
SMTP_USERNAME=
SMTP_PASSWORD=
EMAIL_FROM=
EMAIL_TO=

INPUT_FILE=data/Top_25_HR_Projections__Full_Apex_Stack_.csv
OUTPUT_DIR=output
```

---

## 4. DOCKERFILE

Create `Dockerfile`:

```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "run_apex_daily.py"]
```

---

## 5. README.md

Create `README.md`:

```markdown
# Apex Arc Engine (MLB Home Run Prediction System)

An automated system that:
- Filters confirmed MLB starters
- Generates home run predictions
- Builds optimized parlay stacks
- Narrates top picks
- Supports Discord and email alerts

## How to Run

1. Clone the repo
2. Create `.env` from `.env.template`
3. Build and run with Docker:

```
docker build -t apex-arc .
docker run --env-file .env apex-arc
```
```

---

## 6. GITHUB: Push It Live

```bash
git init
git add .
git commit -m "Initial commit – Apex Arc Engine"
git remote add origin https://github.com/YOUR_USERNAME/apex-arc-engine.git
git push -u origin main
```

---

## 7. OPTIONAL: Run with CRON (Inside Docker)

```bash
0 10 * * * docker run --rm --env-file /full/path/.env apex-arc
```

---

## 8. OPTIONAL: Deploy to Cloud or GitHub Actions

Add `.github/workflows/daily.yml` to run daily with GitHub Actions. Ask if you want this scaffolded too.

---

You're now ready to launch the Apex Arc Engine daily from anywhere.
