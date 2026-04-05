from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    role: str
    is_active: Optional[bool] = True

    # ✅ Validate role
    @field_validator("role")
    def validate_role(cls, value):
        allowed_roles = ["viewer", "analyst", "admin"]
        if value not in allowed_roles:
            raise ValueError("Role must be viewer, analyst, or admin")
        return value