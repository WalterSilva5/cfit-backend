from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(_app: FastAPI):
    print("Setting up!")
    yield
    print("Tearing down!")