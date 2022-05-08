from fastapi import FastAPI

from services.disease_service import router

app = FastAPI()
app.include_router(router, tags=["Api resources"], prefix="/api")
