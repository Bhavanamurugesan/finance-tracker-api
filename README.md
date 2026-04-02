# 💰 Finance Tracker API

## 📌 Project Overview
Finance Tracker API is a backend application built using FastAPI and SQLAlchemy to manage financial transactions efficiently.

It allows users to:
- Add income and expense transactions
- View all transactions
- Delete transactions
- Get a financial summary (income, expenses, balance)

This project demonstrates REST API development, database integration, validation, and clean backend architecture using Python.

---

## 🚀 Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## 📂 Project Structure
```
finance_project/
│
├── main.py          # FastAPI application
├── models.py        # Database models
├── schemas.py       # Data validation schemas
├── crud.py          # Database operations
├── database.py      # DB connection setup
├── requirements.txt # Dependencies
├── .gitignore       # Ignored files
└── README.md        # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/finance-tracker-api.git
```

### 2️⃣ Navigate to project folder
```bash
cd finance_project
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the server
```bash
uvicorn main:app --reload
```

### 5️⃣ Open API docs
👉 http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Check API status |
| POST   | `/transactions` | Create transaction |
| GET    | `/transactions` | Get all transactions |
| DELETE | `/transactions/{id}` | Delete transaction |
| GET    | `/summary` | Get financial summary |

---

## 📊 Example Request

### POST `/transactions`
```json
{
  "amount": 500,
  "type": "expense",
  "category": "food",
  "note": "Lunch"
}
```

---

## 📈 Example Response

### GET `/summary`
```json
{
  "total_income": 2000,
  "total_expense": 500,
  "balance": 1500
}
```

---

## 🧪 Testing
Interactive API documentation is available via Swagger UI:

👉 http://127.0.0.1:8000/docs

---

## 🎯 Key Features
- RESTful API design
- CRUD operations
- Input validation with Pydantic
- Database integration with SQLAlchemy
- Clean and modular structure

---

## 👨‍💻 Author
**Bhavana Murugesan**

---

## 📄 License
This project is for educational and demonstration purposes.
