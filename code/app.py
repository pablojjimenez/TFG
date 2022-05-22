from fastapi import FastAPI

from starlette.requests import Request
from fastapi.exceptions import RequestValidationError
from fastapi.exceptions import StarletteHTTPException, HTTPException
from starlette.responses import Response, JSONResponse

from services.disease_service import dataRouter
from services.managers_service import managersRouter

class validation_exception_handler:
    def __call__(self, request: Request, ex: Exception) -> Response:
        return JSONResponse(
            {
                "error_message": ex.detail,
                "code": 400
            }, status_code=400)


app = FastAPI()
app.include_router(dataRouter, tags=["Api resources"], prefix="/data")
app.include_router(managersRouter, tags=["Api managers"], prefix="/managers")

app.add_exception_handler(HTTPException, validation_exception_handler())
