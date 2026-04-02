from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

# Create tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Finance Tracker API")

# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home route
@app.get("/")
def home():
    return {"message": "Finance Tracker API Running"}

# Create transaction
@app.post("/transactions")
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, transaction)

# Get all transactions
@app.get("/transactions")
def read_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)

# Delete transaction
@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = crud.delete_transaction(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Deleted successfully"}

# Financial summary
@app.get("/summary")
def financial_summary(db: Session = Depends(get_db)):
    transactions = crud.get_transactions(db)

    income = sum(t.amount for t in transactions if t.type == "income")
    expense = sum(t.amount for t in transactions if t.type == "expense")

    balance = income - expense

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": balance
    }