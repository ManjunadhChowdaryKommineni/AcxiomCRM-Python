from datetime import date
from pydantic import BaseModel, Field
class FollowUpIn(BaseModel):
    customer_id: int | None = None
    lead_id: int | None = None
    opportunity_id: int | None = None
    follow_up_date: date
    follow_up_type: str = "Call"
    subject: str = Field(min_length=2, max_length=150)
    remarks: str | None = Field(default=None, max_length=500)
    status: str = "Planned"
    assigned_to: int | None = None
