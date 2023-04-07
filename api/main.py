from fastapi import FastAPI
from modules.users.routes import user_router
from core.config import Config
from db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=Config.HOST,
        port=Config.PORT,
        reload=Config.RELOAD
    )