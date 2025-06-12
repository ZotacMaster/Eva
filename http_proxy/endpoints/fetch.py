from fastapi import APIRouter

from models import ContextQuery, ContextResponse
from utils import context_manger

router = APIRouter()

@router.get("/context/fetch")
async def fetch_context(query: ContextQuery)-> ContextResponse:
    # here check if the context query is in cache if no then check db
    pass