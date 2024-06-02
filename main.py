from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
from src.generators.lifespan import lifespan
from src.modules.user.router import router as user_router


app = FastAPI(
    lifespan=lifespan,
    title="CFIT Backend API",
    description="CFIT Project api documentation",
    version="0.0.1",
    swagger_url="/docs",
    swagger_ui_parameters={
        "syntaxHighlight": {
            "activated": True
        }
    },
    debug = True

)

origins = [
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

app.get("/ping")
async def pong():
    return {"ping": "pong!"}

if __name__ == "__main__":     
    uvicorn.run(app, host="0.0.0.0", port=8000)
