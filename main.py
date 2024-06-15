import uvicorn
from fastapi import  FastAPI
from src.modules.user.router import router as user_router
from src.modules.auth.router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from src.modules.database.db_connection import engine
from src.models import users_model

app = FastAPI(
    title="CFIT Backend API",
    description="CFIT Project API documentation",
    version="0.0.1",
    debug=True,
)


origins = [
    "*",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"]
)

app.include_router(user_router)
app.include_router(auth_router)


users_model.Base.metadata.create_all(bind=engine) 

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


PORT = 8000
HOST = '0.0.0.0' 

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)