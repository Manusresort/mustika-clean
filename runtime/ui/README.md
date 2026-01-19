# Mustika Rasa Human UI

Local-first Human UI for Mustika Rasa governance workflow.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start development server:
```bash
npm run dev
```

The UI will be available at http://localhost:5173

## Backend API

The UI expects the FastAPI backend to be running on http://127.0.0.1:8000

Start the backend:
```bash
cd ..
python -m uvicorn api_server:app --reload --host 127.0.0.1 --port 8000
```

## Build

Build for production:
```bash
npm run build
```

Preview production build:
```bash
npm run preview
```
