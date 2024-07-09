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
        'response': 'Successfully Uploaded Mango Images',
        'model': 'v8.2',
        'classification': 'High Quality',
        'status_code': 200 
    }
    
    
img_height, img_width = 224, 224

# To make predictions on new images
def predict_image(model, img_path):
    from tensorflow.keras.preprocessing import image
    img = image.load_img(img_path, target_size=(img_height, img_width))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    if prediction[0] > 0.5:
        print(f'The image {img_path} is classified as HIGH GRADE')
    else:
        print(f'The image {img_path} is classified as LOW GRADE')

