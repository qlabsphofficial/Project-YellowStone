from fastapi import APIRouter
from database import get_database


router = APIRouter()


@router.get('/')
async def login():
    pass