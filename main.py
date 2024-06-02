import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.generators.lifespan import lifespan
from src.modules.user.router import router as user_router
from src.modules.auth.router import router as auth_router
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    lifespan=lifespan,
    title="CFIT Backend API",
    description="CFIT Project api documentation",
    version="0.0.1",
    debug=True
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="CFIT Backend API",
        version="0.0.1",
        description="CFIT Project api documentation",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=app.title + " - Swagger UI",
        oauth2_redirect_url="/docs/oauth2-redirect",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )

@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    return app.openapi()

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
app.include_router(auth_router)

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)