from fastapi import APIRouter
from typing import Union

router = APIRouter()


@router.get("/")
async def read_root():
    return {"Hello": "World"}

# Las funciones no tienen que ser asincronas obligatoriamnete


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
