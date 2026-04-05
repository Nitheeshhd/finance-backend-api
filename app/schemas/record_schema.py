from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional

class RecordCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: Optional[str] = None

    @field_validator("type")
    def validate_type(cls, value):
        if value not in ["income", "expense"]:
            raise ValueError("Type must be 'income' or 'expense'")
        return value

    @field_validator("amount")
    def validate_amount(cls, value):
        if value <= 0:
            raise ValueError("Amount must be greater than 0")
        return value