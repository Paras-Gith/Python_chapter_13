from pydantic import BaseModel
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantites: Dict[str, int]

class blogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None

Cart_data = {
    "user_id": 123,
    "items": ["Laptop","Mouse","Keyboard"],
    "quantities":{"Laptop":1,"Mouse":2,"Keyboard":3}
}

cart = Cart(**Cart_data)

