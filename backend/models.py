from sqlalchemy import Column, Integer, Text, DateTime, func
from db import Base

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    contact_number = Column(Text, nullable=False)
    user_name = Column(Text)
    product_name = Column(Text)
    product_review = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())