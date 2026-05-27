from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="FVS V2"
)

app.include_router(router)  