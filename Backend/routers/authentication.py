from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_database

from model_classes.auth_models import UserModel
from models import User

router = APIRouter()


@router.post('/login')
async def login(login: UserModel, db: Session = Depends(get_database)):
    try:
        user = db.query(User).filter(User.username == login.username).first()

        if user is not None:
            if user.password == login.password:
                return { 'response': 'Login successful.', 'status': 200 }
            else:
                return { 'response': 'Login Failed.', 'status': 401 }
        else:
            return { 'response': 'Login Failed.', 'status': 401 }
        
    except:
        return { 'response': 'Login Unsuccessful.', 'status': 403 }