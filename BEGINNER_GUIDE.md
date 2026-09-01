# 🎓 Borza Financial Literacy Platform — Beginner's Learning Guide

## What This Project Does
**Borza** is an interactive financial literacy academy, market simulator, spaced-repetition review system, and practical financial decision lab built with FastAPI (Python) and Next.js 16 (React 19 / TypeScript).

---

## 🗺️ Architecture Map

```
BACKEND ARCHITECTURE (FastAPI + SQLAlchemy + Pydantic)
  ├── Content & Quizzes (backend/app/api/v1/endpoints/academy.py)
  ├── Market Simulator & Portfolio Execution (backend/app/services/simulator_engine.py)
  ├── Spaced Repetition Review Engine (backend/app/services/fsrs_service.py)
  └── Practical Finance Tools & Calculators (backend/app/services/calculator_engine.py)

FRONTEND ARCHITECTURE (Next.js 16 + React 19 + Tailwind CSS 4)
  ├── Interactive Simulator (frontend/features/simulator/)
  ├── Academy Lessons & Quizzes (frontend/features/academy/)
  ├── Review System / FSRS (frontend/features/review/)
  └── Financial Decision Lab (frontend/features/practical-finance/)
```

---

## 🎯 Core Files to Study First (Recommended Learning Order)

1. [`backend/app/services/simulator_engine.py`](file:///C:/Users/tinif/repos/Borza/backend/app/services/simulator_engine.py)
   - **Why study first**: Shows how financial market orders, pricing slippage, and portfolio balances are simulated safely in memory/database.
2. [`frontend/features/simulator/engine.ts`](file:///C:/Users/tinif/repos/Borza/frontend/features/simulator/engine.ts)
   - **Why study next**: Teaches client-side state management for financial trading and price feeds.
3. [`backend/tests/test_simulator.py`](file:///C:/Users/tinif/repos/Borza/backend/tests/test_simulator.py)
   - **Why study third**: Demonstrates comprehensive backend testing of order matching, validation, and balance checks.

---

## 🛠️ How to Run & Verify

1. **Backend Tests**:
   ```bash
   cd backend
   .\.venv\Scripts\pytest
   ```
2. **Frontend Tests**:
   ```bash
   cd frontend
   npm test
   ```
