"""
backend/api/main.py

Main FastAPI application for ProspectIQ.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.settings import settings

# Import routers
# Uncomment these as you implement them.
from backend.api.routes.workflow_routes import router as workflow_router
# from backend.api.routes.prospect_routes import router as prospect_router
from backend.api.routes.configuration_routes import router as configuration_router
# from backend.api.routes.analytics_routes import router as analytics_router
# from backend.api.routes.hitl_routes import router as hitl_router
# from backend.api.routes.websocket_routes import router as websocket_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Agentic AI Platform for B2B Prospect Intelligence",
)

# -----------------------------------------------------
# CORS
# -----------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------------------------------
# Events
# -----------------------------------------------------

@app.on_event("startup")
async def startup_event():
    print("ProspectIQ API started.")


@app.on_event("shutdown")
async def shutdown_event():
    print("ProspectIQ API stopped.")


# -----------------------------------------------------
# Health Check
# -----------------------------------------------------

@app.get("/", tags=["Health"])
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "healthy",
    }


# -----------------------------------------------------
# Routers
# -----------------------------------------------------

# Uncomment these as they are implemented.
#
app.include_router(workflow_router, prefix="/api/workflows", tags=["Workflows"])
# app.include_router(prospect_router, prefix="/api/prospects", tags=["Prospects"])
app.include_router(configuration_router, prefix="/api/config", tags=["Configuration"])
# app.include_router(analytics_router, prefix="/api/analytics", tags=["Analytics"])
# app.include_router(hitl_router, prefix="/api/approvals", tags=["Approvals"])
# app.include_router(websocket_router)