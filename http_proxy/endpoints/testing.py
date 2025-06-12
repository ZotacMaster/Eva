from fastapi import APIRouter

from models import ContextQuery, ContextResponse, ContextData
from utils import context_manger

router = APIRouter()

@router.get("/test/fetch")
async def fetch(query: ContextQuery)-> ContextResponse:
    # here check if the context query is in cache if no then check db
    pass

@router.post("/test/update")
async def update(data: ContextData) -> str:
    pass

@router.post("/test/insert")
async def insert(data: ContextData) -> None:
    pass