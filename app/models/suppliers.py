from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, primary_key=True, index=True)
    supplier_name = Column(String, nullable=False, unique=True)
    contact_person = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    # reciprocal relationship with Product
    products = relationship("Product", back_populates="supplier")
