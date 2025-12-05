from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base,Session
from fastapi import FastAPI

app= FastAPI()

Base = declarative_base()
DATABASE_URL = "postgresql+psycopg2://postgres:virat@localhost:5432/classdata"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

def get_db_data():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
