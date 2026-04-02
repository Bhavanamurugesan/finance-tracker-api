from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    note: str
    
class Transaction(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    note: str

    class Config:
        from_attributes = True
