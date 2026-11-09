# Device Job Manager

A full-stack practice project for managing devices and running async jobs, built with FastAPI and Next.js.

## Features

- Register, list, and view devices via REST API
- Request validation with Pydantic
- Interactive API docs with Swagger UI

## Tech Stack

| Area | Technology |
|---|---|
| Backend | Python, FastAPI, Pydantic |
| Frontend | Next.js, React (planned) |

## Project Structure

```text
device-job-manager/
└── backend/
    ├── app/
    │   ├── __init__.py
    │   └── main.py
    └── requirements.txt
```

## Getting Started

### Requirements

- Python 3.12+

### Run the backend

```bash
cd backend
python -m venv .venv
source .venv/Scripts/activate  # Windows (Git Bash)
pip install -r requirements.txt
fastapi dev app/main.py
```

Open http://127.0.0.1:8000/docs to try the API.

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/devices` | List all devices |
| GET | `/devices/{device_id}` | Get a device by ID |
| POST | `/devices` | Create a device |

## Roadmap

- [x] Device API (in-memory storage)
- [ ] SQLite database with SQLAlchemy
- [ ] Async jobs with real-time progress (WebSocket)
- [ ] OAuth / JWT authentication
- [ ] Next.js frontend
