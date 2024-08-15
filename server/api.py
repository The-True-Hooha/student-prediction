from typing import Union, List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    
items = []
    

@app.get("/")
def get_items():
    return {"item": items, "message": "all items retrieved successfully"}

@app.delete("/delete")
def delete():
    return {message: "delete something from the server"}



@app.post("/add")
def add_item(item: Item):
    print(items)
    for check_item in items:
        if check_item.id == item.id:
            raise HTTPException(status_code=400, detail="this items already exist")
    items.append(item)
    print(items)
    return {"message": "item added successfully", "item": item}




@app.put("/edit")
def edit():
    return{message: "edit from the server"}

@app.patch("/edit/1")
def editNumber():
    return {message: 'edited number'}
