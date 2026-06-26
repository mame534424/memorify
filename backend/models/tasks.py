from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from database import Base
import uuid



class Task(Base):

    __tablename__ = "tasks"


    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )


    user_id = Column(
        String,
        ForeignKey("users.id"),
        nullable=False
    )


    title = Column(
        String,
        nullable=False
    )


    description = Column(
        Text,
        nullable=True
    )


    category = Column(
        String,
        default="other"
    )


    priority = Column(
        String,
        default="normal"
    )


    scheduled_time = Column(
        DateTime(timezone=True),
        nullable=True
    )


    status = Column(
        String,
        default="pending"
    )


    raw_input = Column(
        Text
    )


    ai_confidence = Column(
        String
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )