from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.responses import PlainTextResponse

from services.disease_service import router

app = FastAPI()
app.include_router(router, tags=["Api resources"], prefix="/api")


@app.exception_handler(HTTPException)
async def validation_exception_handler(request, exc):
    return {
        "status_code": 400,
        "message": str(exc)
    }
