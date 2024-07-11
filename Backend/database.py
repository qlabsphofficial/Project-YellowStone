from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker, engine
from sqlalchemy import create_engine


DATABASE_URL = f'sqlite:///./test.db'

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# DATABASE ACCESS
def get_database():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()