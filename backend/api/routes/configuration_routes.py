"""
backend/api/routes/configuration_routes.py
"""

from fastapi import APIRouter

from backend.services.configuration_service import configuration_service

router = APIRouter()


@router.get("/icp")
async def get_icp():
    return configuration_service.get_icp()


@router.get("/personas")
async def get_personas():
    return configuration_service.get_personas()


@router.get("/triggers")
async def get_triggers():
    return configuration_service.get_triggers()


@router.get("/workflow")
async def get_workflow():
    return configuration_service.get_workflow()


@router.get("/providers")
async def get_providers():
    return configuration_service.get_providers()


@router.get("/scoring")
async def get_scoring():
    return configuration_service.get_scoring()