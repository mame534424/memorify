from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base
import uuid



class MessageLog(Base):

    __tablename__ = "message_logs"


    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )


    user_id = Column(
        String,
        ForeignKey("users.id")
    )


    direction = Column(
        String
    )


    content = Column(
        Text,
        nullable=False
    )


    intent = Column(
        String
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )