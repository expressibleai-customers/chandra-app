# Generated API Code

## FastAPI Application

This FastAPI application was auto-generated from API contract specifications.

### Models Generated

- UserManagement
- ResourceManagement
- CommunityPlatform
- AIAssistant
- CareProviderPortal

### Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will run on http://localhost:8000

### API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Project Structure

```
api/
├── models/           # Pydantic models
├── routers/          # API endpoints
├── database/         # SQLAlchemy models
├── main.py          # FastAPI app
├── requirements.txt
└── README.md
```

### Database Configuration

Set the DATABASE_URL environment variable:

```bash
export DATABASE_URL="postgresql://user:password@localhost/dbname"
```
