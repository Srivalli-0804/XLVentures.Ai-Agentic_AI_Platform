"""
backend/api/main.py

Main FastAPI application for ProspectIQ.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes.configuration_routes import router as configuration_router
from backend.api.routes.prospect_routes import router as prospect_router
from backend.api.routes.workflow_routes import router as workflow_router
from backend.core.settings import settings
from backend.memory.short_term.session_memory import session_memory

@asynccontextmanager
async def lifespan(app: FastAPI):
    seed_demo_workflow()
    print("ProspectIQ API started.")
    yield
    print("ProspectIQ API stopped.")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Agentic AI Platform for B2B Prospect Intelligence",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def seed_demo_workflow() -> None:
    if session_memory.load("demo-workflow") is None:
        session_memory.save(
            "demo-workflow",
            {
                "workflow_name": "Demo Prospect Sweep",
                "status": "COMPLETED",
                "created_at": "2026-06-29T00:00:00",
                "context": {
                    "discovered_companies": [
                        {
                            "company_id": "comp-1",
                            "name": "Northstar Labs",
                            "industry": "AI Infrastructure",
                            "score": 88,
                        }
                    ],
                    "qualified_companies": [
                        {
                            "company_id": "comp-2",
                            "name": "Vertex AI",
                            "industry": "Automation",
                            "score": 92,
                            "prospect_score": 92,
                        }
                    ],
                    "company_profiles": [
                        {
                            "company_id": "comp-3",
                            "company_name": "Horizon Cloud",
                            "industry": "SaaS",
                            "prospect_score": 90,
                        }
                    ],
                    "recommendations": [
                        {
                            "company_id": "comp-4",
                            "company_name": "Signal Forge",
                            "industry": "Fintech",
                            "prospect_score": 94,
                        }
                    ],
                    "execution_history": [
                        {
                            "agent": "TriggerMonitorAgent",
                            "status": "COMPLETED",
                            "details": "Detected funding and hiring signals",
                            "timestamp": "2026-06-29T00:00:00",
                        },
                        {
                            "agent": "CompanyDiscoveryAgent",
                            "status": "COMPLETED",
                            "details": "Resolved 4 high-intent prospects",
                            "timestamp": "2026-06-29T00:01:00",
                        },
                        {
                            "agent": "ICPQualifierAgent",
                            "status": "COMPLETED",
                            "details": "Qualified 2 matching accounts",
                            "timestamp": "2026-06-29T00:02:00",
                        },
                    ],
                },
            },
        )


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


app.include_router(workflow_router, prefix="/api")
app.include_router(prospect_router, prefix="/api")
app.include_router(configuration_router, prefix="/api")