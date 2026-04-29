from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []


    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )                                                   

user =  User(
    id=1,
    name="Paras",
    email="P@gmail.ai",
    createdAt=datetime(2024, 3, 15, 14, 30, 20),
    address=Address(
        street="Somthing",
        city="Haldwani",
        zip_code="23134"
    ),
    is_active=False,
    tags=["premium", "player"]
)

python_dict = user.model_dump() # this a primary way to convert a sub model to dict
print(python_dict)
print(user)
print("="*30)

json_str = user.model_dump_json() #this convert the model directly in to the json encoded string 
print("="*30)
print(json_str)