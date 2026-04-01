# Finance Tracker API

## 📌 Project Overview

Finance Tracker API is a simple backend application built using **FastAPI** and **SQLAlchemy** that helps users manage their financial transactions.

The API allows users to:

* Add income or expense transactions
* View all transactions
* Delete transactions
* Get a financial summary including total income, total expenses, and balance

This project demonstrates **REST API development, database integration, data validation, and backend application design using Python**.

---

## 🚀 Technologies Used

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

---

## 📂 Project Structure

```
finance_project/
│
├── main.py          # Main FastAPI application
├── models.py        # Database models
├── schemas.py       # Pydantic schemas for validation
├── crud.py          # Database operations
├── database.py      # Database connection setup
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/finance-tracker-api.git
```

### 2️⃣ Navigate to project folder

```
cd finance_project
```

### 3️⃣ Install required dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the server

```
uvicorn main:app --reload
```

### 5️⃣ Open API documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

| Method | Endpoint                       | Description              |
| ------ | ------------------------------ | ------------------------ |
| GET    | /                              | Check if API is running  |
| POST   | /transactions                  | Create a new transaction |
| GET    | /transactions                  | Get all transactions     |
| DELETE | /transactions/{transaction_id} | Delete a transaction     |
| GET    | /summary                       | Get financial summary    |

---

## 📊 Example Transaction Request

POST `/transactions`

```
{
  "amount": 500,
  "type": "expense",
  "category": "food",
  "note": "Lunch"
}
```

---

## 📈 Example Summary Response

GET `/summary`

```
{
  "total_income": 2000,
  "total_expense": 500,
  "balance": 1500
}
```

---

## 🧪 API Testing

This project uses **automatic API documentation** provided by FastAPI through Swagger UI.

You can test all endpoints here:

```
http://127.0.0.1:8000/docs
```

---

## 🎯 Project Purpose

This project was created as a **Python backend development assessment** to demonstrate:

* API design using FastAPI
* Backend logic implementation
* Database integration using SQLAlchemy
* Data validation using Pydantic
* Clean project structure and documentation

---

## 👨‍💻 Author

Bhavana

---
## 📄 License
This project is developed for educational and demonstration purposes as part of a backend development assessment.
