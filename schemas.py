"""
Database Schemas for Insight

Each Pydantic model maps to a MongoDB collection (lowercased class name).
Use these models to validate data before storing in the database.
"""
from typing import List, Optional
from pydantic import BaseModel, Field

class IncidentReport(BaseModel):
    student_id: Optional[str] = Field(None, description="Optional identifier for the student (email, id, etc.)")
    title: str = Field(..., description="Short title for the incident")
    description: str = Field(..., description="What happened")
    feelings: List[str] = Field(default_factory=list, description="List of feelings experienced")
    triggers: List[str] = Field(default_factory=list, description="Possible triggers")
    actions_taken: List[str] = Field(default_factory=list, description="Actions taken during or after the incident")
    support_requested: Optional[str] = Field(None, description="What help is needed")

class BehaviorStep(BaseModel):
    label: str = Field(..., description="Step label")
    done: bool = Field(False, description="Whether the step is completed")

class BehaviorPlan(BaseModel):
    student_id: Optional[str] = Field(None, description="Optional identifier for the student")
    goal: str = Field(..., description="Main behaviour goal")
    strategies: List[str] = Field(default_factory=list, description="Strategies to try")
    steps: List[BehaviorStep] = Field(default_factory=list, description="Actionable steps")
    check_in_frequency: str = Field("daily", description="How often to check in (daily/weekly)")

# Example schemas retained for reference (not used by the app)
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = None
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category: str
    in_stock: bool = True
