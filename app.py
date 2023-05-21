import uuid
from flask import Flask,request
from db import items,stores
from flask_smorest import abort
app = Flask(__name__)

@app.get("/store")
def store():
    return{"stores":list[stores.values]}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id":store_id} # ** unpacks values in the store dict and include them in new dict
    stores[store_id]  = store
    return store, 201

@app.post("/item")
def create_iteam(name):
    iteam_data = request.get_json()
    if iteam_data["store_id"] not in stores:
        abort(404,message="Store not found")
    
    item_id = uuid.uuid4().hex
    item = {**iteam_data, "id": item_id}
    item[item_id] = item
    return item, 201

@app.get("/item")
def get_all_items():
    return{"items", list(items.values())}

@app.get("/store/<string:store_id>")
def get_all_stores(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404,message="Store not found")
                    
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404,message="Store not found")

         
