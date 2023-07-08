from typing import List, Dict, Any
from pydantic import BaseModel

from factory import create_app
from lib.controller import APIController

app =  create_app()
app.controller = APIController()

# this model is used only for the function named get_spesificied_floor to receive all data for the single floor
class FloorModel(BaseModel):
    _id: str
    TOPIC: str
    VALUES: Any

# display only topics
@app.get("/api/topiclist")
async def get_all_topics() -> List[Dict]:
    documents = list(app.controller.mongo_client.collection.find({}, {"_id":0, "VALUES":0}))

    if documents:
        return documents
    else:
        return {"error": "No documents found"}
    
# display topics and their corresponding values
@app.get("/api/alldatalist")
async def get_all_documents() -> List[Dict]:
    documents = list(app.controller.mongo_client.collection.find({},{"_id":0}))

    if documents:
        return documents
    else:
        return {"error": "No documents found"}

# display list of desks specified by a floor
@app.get("/api/{floor}", response_model=List[FloorModel])
async def get_spesificied_floor(floor:str) -> List[Dict]:
    pattern = f'^{floor}'
    documents = list(app.controller.mongo_client.collection.find({"TOPIC": {"$regex": pattern}}))

    if documents:
        return documents
    else:
        return []

# display list of desks spesified by a table
@app.get("/api/{floor}/{desk}")
async def get_spesific_floor(floor:str, desk:str) -> List[FloorModel]:
    pattern = f'^{floor+"/"+desk}'
    print(pattern)
    documents = list(app.controller.mongo_client.collection.find({"TOPIC": {"$regex": pattern}}))

    if documents:
        return documents
    else:
        return []
