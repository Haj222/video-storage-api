from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime
from fastapi import Query

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "mp3")            
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "videos")  

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome !"}

class VideoData(BaseModel):
    filename: str
    s3_path: str

@app.post("/video/upload")
async def upload_video(video: VideoData):
    video_doc = {
        "filename": video.filename,
        "s3_path": video.s3_path,
        "timestamp": datetime.utcnow()
    }
    result = collection.insert_one(video_doc)
    if result.inserted_id:
        return {
            "result": "success",
            "message": "Video stored.",
            "data": {"id": str(result.inserted_id)}
        }
    else:
        raise HTTPException(status_code=500, detail="Failed to store video  .")

@app.get("/video/search")
async def search_video(search_term: str = Query(..., description="Please enter the term to search videos by filename")):
    
    result = collection.find_one({"filename": {"$regex": search_term, "$options": "i"}})
    if result:
        return {
            "result": "success",
            "message": "Video found.",
            "data": {
                "video_path": result["s3_path"]
            }
        }
    else:
        return {
            "result": "fail",
            "message": f"No video found for the search term '{search_term}'.",
            "data": {}
        }
