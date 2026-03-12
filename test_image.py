#어떻게 동작되는지 테스트용 .py파일

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel) :
    name : str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post ("/items/item_id")
def create_item(item_id: int):
    return {"item_id": item_id}

@app.post ("/items/")
def create_item(item: Item):
    return {item}

