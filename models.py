from sqlalchemy import Column, Integer, String, Float
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    note = Column(String, nullable=True)
