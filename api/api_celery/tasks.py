import time
from datetime import datetime
from .worker import celery
from modules.logs.models import Log
from db.database import SessionLocal

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth number.
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

@celery.task
def logging():
    start = datetime.now()
    fibonacci(1000000)
    end = datetime.now()
    print("@@", end - start)
    # db = SessionLocal()
    # log = Log()
    # log.message = str(id(db))
    # db.add(log)
    # db.commit()