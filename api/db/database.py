import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import Config

def wait_for_engine(db_url: str, retries: int = 3) -> None:
    engine = None
    while retries > 0:
        try:
            engine = create_engine(db_url)
            engine.connect()
            break
        except Exception:
            retries -= 1
            time.sleep(5)
    if engine is None:
        raise Exception("Failed to connect to PostgreSQL")

engine_url = f"postgresql://{Config.POSTGRES_USER}:{Config.POSTGRES_PASSWORD}@postgresql:5432/{Config.POSTGRES_DB}"
wait_for_engine(engine_url)

engine = create_engine(engine_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()