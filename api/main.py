from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import user_management

from .routers import resource_management

from .routers import community_platform

from .routers import ai_assistant

from .routers import care_provider_portal


app = FastAPI(
    title="Generated API",
    version="1.0.0",
    description="Auto-generated API from specifications"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers

app.include_router(user_management.router, prefix="/api")

app.include_router(resource_management.router, prefix="/api")

app.include_router(community_platform.router, prefix="/api")

app.include_router(ai_assistant.router, prefix="/api")

app.include_router(care_provider_portal.router, prefix="/api")


@app.get("/")
def root():
    return {
        "message": "API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}