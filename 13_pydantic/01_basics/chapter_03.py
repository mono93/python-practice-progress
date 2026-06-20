from pydantic import BaseModel
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


cart_input = {
    "user_id": 1,
    "items": ["laptop", "monitor", "speaker"],
    "quantities": {"laptop": 1, "monitor": 2, "speaker": 3}
}

cart_1 = Cart(**cart_input)
print(cart_1)

