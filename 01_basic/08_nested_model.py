from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address # this user also have address model as Address not a str


address = Address(
    street="123 something",
    city="Jaipur",
    postal_code="100001"
)


user = User(
    id=1,
    name="Paras",
    address=address,
)

user_data = {
    "id": 1,
    "name": "Paras",
    "address":{
        "street": "321 something",
        "city": "Paris",
        "postal_code": "2003"
    }
}

user =  User(**user_data)
print(user)
