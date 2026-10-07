from pydantic import BaseModel, EmailStr, Field, field_validator
import re
class LeadIn(BaseModel):
    lead_name: str = Field(min_length=2, max_length=150)
    email: EmailStr
    phone: str = Field(min_length=7, max_length=20)
    company_name: str | None = Field(default=None, max_length=150)
    source: str = Field(default="Website", max_length=50)
    status: str = Field(default="New", max_length=30)
    priority: str = Field(default="Medium", max_length=20)
    expected_value: float = Field(default=0, ge=0)
    assigned_to: int | None = None
    @field_validator("phone")
    @classmethod
    def valid_phone(cls, v):
        if not re.fullmatch(r"[0-9+() -]{7,20}", v): raise ValueError("Invalid phone number")
        return v
