from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime


#this is called multiple field validation
class Person(BaseModel):
    first_name: str
    Last_name: str


    @field_validator('first_name', 'Last_name')
    def name_must_be_capitalize(cls, v):
        if not v.istitle():
            raise ValueError('Name must be Capitialized')
        return

#data transformation pattern
class User(BaseModel):
    email: str


    @field_validator('email')
    def normalize_email(cls, v):
        if not v.istitle():
            raise ValueError('Name must be capitalized')
        return v.lower().strip()
    

#if you want to run the value befor the validator
class Product(BaseModel):
    price: str

    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v
    
#complex model validation
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime


    @model_validator(mode='after')
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError('end_date must be after start date')
        return values