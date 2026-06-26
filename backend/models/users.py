from sqlalchemy import Column, String, BigInteger, DateTime
from sqlalchemy.sql import func
from database import Base
import uuid


class User(Base):

    __tablename__ = "users"


    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )


    telegram_id = Column(
        BigInteger,
        unique=True,
        nullable=False
    )


    username = Column(
        String,
        nullable=True
    )


    first_name = Column(
        String,
        nullable=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )