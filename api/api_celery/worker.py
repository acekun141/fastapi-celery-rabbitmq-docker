from celery import Celery
from core.config import Config

celery = Celery("celery_worker", broker=Config.CELERY_BROKER_URL)
celery.autodiscover_tasks(["api_celery"])