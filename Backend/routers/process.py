from fastapi import APIRouter, File, UploadFile, Depends, HTTPException, status
from sqlalchemy import func, asc, desc
from sqlalchemy.orm import Session

from typing import List
from database import get_database
from models import Record

from datetime import datetime, timedelta
import random
import calendar

import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image
import io

router = APIRouter()

# Load your model once
model = load_model('./final_mango_quality_model.h5')
img_height, img_width = 224, 224

def predict_image(model, img_bytes):
    img = Image.open(io.BytesIO(img_bytes))
    img = img.resize((img_height, img_width))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    print(prediction)
    
    if prediction[0] < 0.70:
        return 'High Quality'
    else:
        return 'Low Quality'


@router.post('/handle_image_payload')
async def handle_image_payload(images: List[UploadFile] = File(...), db: Session = Depends(get_database)):
    quality_count = 0
    analysis = 'Low Quality'
    
    for image in images:
        contents = await image.read()
        classification = predict_image(model, contents)
        print(classification)
        
        if classification == 'High Quality':
            quality_count += 1
            
    
    if quality_count >= 2:
        analysis = 'High Quality'
        
    record = Record()
    record.analysis = analysis
    
    db.add(record)
    db.commit()

    return { 
        'response': 'Successfully Uploaded Mango Images',
        'analysis': analysis,
        'status_code': 200 
    }
    
@router.get('/retrieve_dashboard_data')
async def retrieve_dashboard_data(db: Session = Depends(get_database)):
    try:
        analysis = db.query(func.avg(Record.analysis)).scalar()
        
        hq = db.query(Record).filter(Record.analysis == 'High Quality').count()
        lq = db.query(Record).filter(Record.analysis == 'Low Quality').count()
        
        current_date = datetime.now()
        current_month = current_date.month
        current_year = current_date.year

        # Calculate months from current month to 5 months before
        months = []
        for i in range(5, -1, -1):
            month = current_month - i
            year = current_year
            if month <= 0:
                month += 12
                year -= 1
            months.append((month, year))

        month_data = []
        for month, year in months:
            first_day_of_month = datetime(year, month, 1)
            last_day_of_month = datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)

            total_hq = db.query(Record).filter(
                Record.analysis == 'High Quality',
                Record.date_recorded >= first_day_of_month,
                Record.date_recorded <= last_day_of_month
            ).count()

            total_lq = db.query(Record).filter(
                Record.analysis == 'Low Quality',
                Record.date_recorded >= first_day_of_month,
                Record.date_recorded <= last_day_of_month
            ).count()
            
            summation = total_hq + total_lq
            
            month_data.append({
                'month': first_day_of_month.strftime('%B %Y'),
                'hq_count': total_hq,
                'hq_percent': round((total_hq / summation) * 100, 2),
                'lq_count': total_lq,
                'lq_percent': round((total_lq / summation) * 100, 2)
            })
        
        general_report = f"""
            As of {datetime.now()}, there are {hq} number of high quality mangoes analyzed by the system.
            There are also {lq} number of low quality mangoes analyzed by the system. The total number of analyzed mangoes 
            within the system is {hq+lq}.
        """
        
        payload = {
            'hq': hq,
            'lq': lq,
            'month_data': month_data,
            'analysis': analysis,
            'general_report': general_report
        }

        return { 'payload': payload, 'status_code': 200 }
    except Exception as e:
        return { 'response': f'Error retrieving data: {str(e)}', 'status_code': 400 }


@router.get('/retrieve_records')
async def retrieve_records(db: Session = Depends(get_database)):
    try:
        records = db.query(Record).order_by(Record.date_recorded.desc()).all()

        return { 'payload': records, 'status_code': 200 }
    except Exception as e:
        return { 'response': f'Error retrieving data: {str(e)}', 'status_code': 400 }
    

# GENERATE DATA
@router.post("/generate_records/")
def generate_records(db: Session = Depends(get_database)):
    try:
        records_to_create = 5000
        today = datetime.now()

        # Generate 5000 records
        records = []
        for _ in range(records_to_create):
            analysis = random.choice(["High Quality", "Low Quality"])
            date_recorded = today - timedelta(days=random.randint(1, 365))

            record = Record(analysis=analysis, date_recorded=date_recorded)
            records.append(record)

        # Bulk insert records into database
        db.bulk_save_objects(records)
        db.commit()

        return {"message": f"Successfully generated and saved {records_to_create} records."}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))