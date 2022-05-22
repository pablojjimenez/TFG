from json import JSONDecodeError
from fastapi import APIRouter, HTTPException
from fastapi.exceptions import RequestValidationError


managersRouter = APIRouter(
    responses={404: {"description": "Not found"}}
)

@managersRouter.get("/test", status_code=200)
def prueba():
    return {
        'hola': 'adios'
    }