from fastapi import APIRouter
from models import HealthCheck

router = APIRouter()

@router.get("/health")
async def fetch_context()-> HealthCheck:
    # basic API healthcheck
    pass