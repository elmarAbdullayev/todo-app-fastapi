from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    username = Column(String(50),nullable=False,unique=True)
    password = Column(String(100),nullable=False)
    tasks = relationship("Task",back_populates="user",cascade="all,delete")



