from pydantic import BaseModel, EmailStr, Field, field_validator
import re
class CustomerIn(BaseModel):
    customer_name: str = Field(min_length=2, max_length=150)
    email: EmailStr
    phone: str = Field(min_length=7, max_length=20)
    company_name: str = Field(min_length=2, max_length=150)
    address: str | None = Field(default=None, max_length=250)
    city: str | None = Field(default=None, max_length=100)
    state: str | None = Field(default=None, max_length=100)
    status: str = Field(default="Active", max_length=30)
    @field_validator("phone")
    @classmethod
    def valid_phone(cls, v):
        if not re.fullmatch(r"[0-9+() -]{7,20}", v): raise ValueError("Invalid phone number")
        return v
