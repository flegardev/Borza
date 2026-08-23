# Borza Financial Academy

Multilingual financial literacy academy with micro-learning courses, paper trading simulator, FastAPI, and Next.js.

![Borza Academy Branding](docs/brand/tini-flegar-profile-dark.png)

## Overview

**Borza** is an interactive financial literacy platform and paper trading simulator. Built with a Next.js TypeScript frontend and a Python FastAPI backend, it combines structured micro-learning courses (covering budgeting, stock markets, crypto, and portfolio risk) with a real-time paper trading engine for practicing investment strategies with virtual funds.

## Key Features

* **Structured Micro-Learning Modules**: Interactive lesson slides, financial vocabulary flashcards, and knowledge assessment quizzes.
* **Real-Time Paper Trading Simulator**: Practice buying and selling stocks/ETFs using simulated market pricing and portfolio tracking.
* **Portfolio Risk Analytics**: Visual pie chart asset distribution, profit/loss (P&L) performance tracking, and transaction logs built with Recharts.
* **FastAPI Microservices**: Asynchronous Python REST API (`backend/`) powered by Pydantic models and SQLAlchemy.
* **Multilingual Localization Support**: Internationalized content structure supporting multiple languages.

## Tech Stack

**Frontend (`/frontend`)**
* Next.js (App Router), React, TypeScript
* Tailwind CSS, Lucide React, Recharts

**Backend (`/backend`)**
* FastAPI, Python 3.11, Pydantic, SQLAlchemy / AsyncPG

**Database & Infrastructure**
* PostgreSQL, Redis
* Docker Compose, Render (`render.yaml`)

## System Architecture

```mermaid
flowchart TD
    NextFrontend["Next.js Web App (Academy & Simulator)"]
    FastAPI["FastAPI Python Engine"]
    Postgres[(PostgreSQL Database)]
    Redis[(Redis Cache)]
    MarketData["Market Price API Service"]

    NextFrontend -->|REST API| FastAPI
    FastAPI -->|User Progress & Trades| Postgres
    FastAPI -->|Session & Quote Cache| Redis
    FastAPI -->|Live Price Feeds| MarketData
```

## Getting Started

### Prerequisites
* Node.js 18+
* Python 3.11+
* Docker Desktop (optional)

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/flegardev/Borza.git
   cd Borza
   ```

2. Start services with PowerShell script (Windows):
   ```powershell
   .\start-local.ps1
   ```

3. Or launch using Docker Compose:
   ```bash
   docker compose up -d
   ```

## Environment Variables

```env
DATABASE_URL=postgresql://user:pass@localhost:5432/borza
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your_development_secret_key
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Deployment

Deployed on Vercel at [https://borza-kappa.vercel.app](https://borza-kappa.vercel.app).

## License

This project is licensed under the MIT License.
