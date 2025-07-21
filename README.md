# video-storage-api
This project is a FastAPI backend service that uploads video metadata and search videos by filename. The video information is stored in a MongoDB database for futher analytics/usage. 

# Features 
Upload video metadata (filename and S3 path)  
Search videos by filename   
Stores upload timestamps automatically  
Configurable MongoDB connection via environment variables  
MongoDB Compass is not necessary, but useful for database management and inspection  


# Dependencies 
Python 3.7+  
MongoDB instance (local or cloud)  
MongoDB Compass 
`pip` package manager (in order to install: fastapi, uvicorn, pymongo, python-dotenv)


# Setup

 1. Clone the repository
    git clone https://github.com/Haj222/video-storage-api.git
    cd video-storage-api

 2. Create and activate a Python virtual environment
    python3 -m venv venv
    source venv/bin/activate  #This command is used for individulas who use Mac 

 3. Install dependencies
    pip install fastapi uvicorn pymongo python-dotenv

 4. Run program on your local device 
