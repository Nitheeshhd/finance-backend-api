💰 Finance Backend API

A simple backend system built using FastAPI to manage users, financial records, and provide dashboard analytics with role-based access control.

---

## 🚀 Features

- 👤 User and Role Management (Admin, Analyst, Viewer)
- 📊 Financial Records CRUD (Create, Read, Update, Delete)
- 🔍 Record Filtering (by type and category)
- 📈 Dashboard APIs (Total Income, Expense, Balance)
- 🔐 Role-Based Access Control (Middleware)
- ✅ Input Validation and Error Handling (Pydantic)

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

---

## 📁 Project Structure


finance-backend/
│
├── app/
│ ├── main.py
│ ├── routes/
│ ├── models/
│ ├── schemas/
│ ├── services/
│ └── middleware/
│
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the repository


git clone https://github.com/Nitheeshhd/finance-backend-api.git

cd finance-backend-api


---

### 2. Create virtual environment


python -m venv venv
venv\Scripts\activate


---

### 3. Install dependencies


pip install -r requirements.txt


---

### 4. Run the server


uvicorn app.main:app --reload


---

### 5. Open Swagger Docs


http://127.0.0.1:8000/docs


---

## 📊 API Endpoints

### 👤 Users
- POST `/users` → Create user
- GET `/users` → Get users

---

### 💰 Records
- POST `/records` → Add record
- GET `/records` → Get all records
- PUT `/records/{index}` → Update record
- DELETE `/records/{index}` → Delete record
- GET `/records/filter` → Filter records

---

### 📈 Dashboard
- GET `/dashboard/income`
- GET `/dashboard/expense`
- GET `/dashboard/balance`

---

## 🔐 Role-Based Access

- Admin → Full access
- Analyst → Read-only
- Viewer → Read-only (GET only)

---

## ⚠️ Note

- Data is stored in-memory (Python list)
- Data will reset when server restarts
- Can be extended to use databases like PostgreSQL or MongoDB

---

## 📸 Screenshots

(Add your Swagger screenshots here)

---

## 👨‍💻 Author

**Nitheesh H D**
GitHub: https://github.com/Nitheeshhd

---

## 🎯 Conclusion

This project demonstrates a complete backend system with clean architecture, validation, role-based access, and real-world API design using FastAPI.
