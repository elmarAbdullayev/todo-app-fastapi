from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True)
    title = Column(String(50),nullable=False)
    description = Column(String(50), nullable=False)
    completed  = Column(Boolean, nullable=False, default=False)
    user_id  = Column(Integer, ForeignKey("users.id"),nullable=False)
    user = relationship("User",back_populates="tasks")