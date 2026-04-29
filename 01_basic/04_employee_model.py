from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples=["Paras Nainwal"]
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000        #ge mean greater then
    )

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r'^[\w\.-]+@[\w\.-]+\.\w+$',
        description="Valid email address",
        examples=["user@example.com"]
    )

    phone: str = Field(
        ...,
        regex=r'^\+?\d{10,15}$',
        description="Phone number with optional country code",
        examples=["+919000000000", "9000000000"]
    )
    age:  int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount Perscentage"
    )



