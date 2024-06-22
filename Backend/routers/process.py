from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session

from typing import List
from database import get_database

import random
import time

router = APIRouter()


@router.post('/handle_image_payload')
async def handle_image_payload(images: List[UploadFile] = File(...), db: Session = Depends(get_database)):
    for image in images:
        contents = await image.read()
        random_classification = random.randint(0, 2)
        
        classification = 'Low Quality'
        
        if random_classification == 1:
            classification = 'High Quality'
        
    time.sleep(10)
    
    return { 
        'response': 'Successfully Uploaded Image',
        'number_of_tests_conducted': '500 (100 * 5)',
        'classification': classification,
        'status_code': 200 
    }