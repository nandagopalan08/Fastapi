from fastapi import FastAPI

app = FastAPI()
items_db = []

@app.post("/items/")
def create_item(item: dict):
    if any(existing_item["id"] == item["id"] for existing_item in items_db):
        return {"status": "error", "message": "Item ID already exists"}
    items_db.append(item)
    return {"status": "success", "message": "Item created successfully", "item": item}

@app.get("/items/")
def read_items():
    return {"status": "success", "items": items_db}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = next((item for item in items_db if item["id"] == item_id), None)
    if not item:
        return {"status": "error", "message": "Item not found"}
    return {"status": "success", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: dict):
    for index, item in enumerate(items_db):
        if item["id"] == item_id:
            items_db[index] = updated_item
            return {"status": "success", "message": "Item updated successfully", "item": updated_item}
    return {"status": "error", "message": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item["id"] == item_id:
            del items_db[index]
            return {"status": "success", "message": "Item deleted successfully"}
    return {"status": "error", "message": "Item not found"}