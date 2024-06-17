from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session

from typing import List

from database import get_database


router = APIRouter()


@router.post('/handle_image_payload')
async def handle_image_payload(images: List[UploadFile] = File(...), db: Session = Depends(get_database)):
    for image in images:
        contents = await image.read()
        print(contents)
    
    return { 'response': 'test works', 'status_code': 200 }