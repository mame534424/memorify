from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base
import uuid



class Memory(Base):

    __tablename__ = "memories"


    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )


    user_id = Column(
        String,
        ForeignKey("users.id")
    )


    content = Column(
        Text,
        nullable=False
    )


    category = Column(
        String
    )


    source = Column(
        String,
        default="telegram"
    )


    raw_input = Column(
        Text
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )