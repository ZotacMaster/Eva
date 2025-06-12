from fastapi import APIRouter

from models import ContextQuery, ContextResponse, ContextData
from utils import context_manger

router = APIRouter()

@router.get("/context/insert")
async def insert_context(query: ContextData)-> ContextResponse:
    # here check if the context query is in cache if no then check db
    pass