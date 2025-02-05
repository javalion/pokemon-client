from pydantic import BaseModel

class Pokemon(BaseModel):
    id: str
    category: str
    illustrator: str
    image: str
    localId: str
    name: str
    rarity: str
