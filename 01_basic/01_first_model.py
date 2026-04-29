from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool    #it is a field

input_data = {'id': 101, 'name': "chaicode", 'is_active': True} # if you change the value of the set value to another datatype it will give pydantic error

user = User(**input_data)   #(**) it mean unpack the library
print(user)
