from fastapi import APIRouter, logger
from api_celery.tasks import logging


user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@user_router.get("/")
async def get_user():
    for i in range(100):
        task = logging.delay()
        print(i, task.id)
    return "Done"