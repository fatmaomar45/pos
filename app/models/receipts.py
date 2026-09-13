from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Receipt(Base):
    __tablename__ = "receipts"

    receipt_id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.sale_id"), nullable=False)
    receipt_number = Column(String, nullable=False, unique=True)
    issue_date = Column(DateTime(timezone=True), server_default=func.now())

    
    sale = relationship("Sale", back_populates="receipts")
