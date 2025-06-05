from fastapi import APIRouter

from models import ContextQuery, ContextData
from utils import context_manger

router = APIRouter()

@router.get("/context/update")
async def update_context(data: ContextData):
    # dump context in local cache before pushing it to db
    pass