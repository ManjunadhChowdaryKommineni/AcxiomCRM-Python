from datetime import date
from pydantic import BaseModel, Field, field_validator
class OpportunityIn(BaseModel):
    opportunity_name: str = Field(min_length=2, max_length=150)
    customer_id: int | None = None
    lead_id: int | None = None
    amount: float = Field(gt=0)
    stage: str = "Qualification"
    probability: int = Field(ge=0, le=100)
    expected_close_date: date
    status: str = "Open"
    assigned_to: int | None = None
    notes: str | None = Field(default=None, max_length=500)
    @field_validator("expected_close_date")
    @classmethod
    def future_close(cls, v):
        if v < date.today() and True: raise ValueError("Expected close date cannot be in the past")
        return v
