from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., title="Item name", regex=r"[A-Z][A-Za-z0-9]+", max_length=12)
    description: Optional[str] = Field(
        None, title="The description of the item",
        max_length=300,
    )
    price: float = Field(...,
                         gt=0,
                         description="The price must be greater than zero",
                         )
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int,
                      item: Item = Body(..., embed=True)
                      ):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/items/")
async def new_item(
                   item: Item = Body(..., embed=True)
                   ):
    results = {"item": item}
    return results
