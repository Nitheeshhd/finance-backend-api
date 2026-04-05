from fastapi import APIRouter
from app.models.record_model import records_db

router = APIRouter()

# Total Income
@router.get("/dashboard/income")
def total_income():
    income = sum(record["amount"] for record in records_db if record["type"] == "income")
    return {"total_income": income}

# Total Expense
@router.get("/dashboard/expense")
def total_expense():
    expense = sum(record["amount"] for record in records_db if record["type"] == "expense")
    return {"total_expense": expense}

# Net Balance
@router.get("/dashboard/balance")
def net_balance():
    income = sum(record["amount"] for record in records_db if record["type"] == "income")
    expense = sum(record["amount"] for record in records_db if record["type"] == "expense")
    return {"net_balance": income - expense}