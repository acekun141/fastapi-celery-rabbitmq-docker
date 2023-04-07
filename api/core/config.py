import os


class Config:
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
    HOST = os.environ.get("HOST")
    PORT = int(os.environ.get("PORT"))
    RELOAD = bool(int(os.environ.get("RELOAD")))
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")