from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, DECIMAL
from enum import Enum as PyEnum
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from app.models import Base

class OperationType(PyEnum):
    BUY = "buy"
    SELL = "sell"

class Bid(Base):
    __tablename__ = "bids"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    price = Column(DECIMAL(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    time_slot = Column(Integer, nullable=False)
    day = Column(DateTime, nullable=False)
    iso = Column(String, nullable=False)
    operation = Column(Enum(OperationType), nullable=False)

    user = relationship("User", back_populates="bids")
