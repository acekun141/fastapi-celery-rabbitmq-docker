from sqlalchemy import Column, ForeignKey, Integer, String
from db.database import Base

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)