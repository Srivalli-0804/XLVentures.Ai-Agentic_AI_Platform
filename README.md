# ProspectIQ

A polished agentic AI prospect intelligence platform with a FastAPI backend and a Vite + React frontend.

## Run the backend

```bash
cd backend
python -m uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

## Run the frontend

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 3000
```

## Verify

- Backend health: http://localhost:8000/health
- Frontend: http://localhost:3000
