import strawberry
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from starlette.requests import Request
from fastapi.exceptions import HTTPException
from starlette.responses import Response, JSONResponse
from strawberry.asgi import GraphQL

from graphql_services.graphql_mutations import Mutation
from graphql_services.grapql_types import Query
from models.openapi_models.models import get_extra_models
from services.disease_service import dataRouter
from services.managers_service import managersRouter


class validation_exception_handler:
    def __call__(self, request: Request, ex: Exception) -> Response:
        return JSONResponse({
            "error_message": ex.detail,
            "code": ex.status_code
        }, status_code=ex.status_code)


app = FastAPI()
app.include_router(dataRouter, tags=["Api resources"], prefix="/data")
app.include_router(managersRouter, tags=["Api managers"], prefix="/managers")
app.add_exception_handler(HTTPException, validation_exception_handler())

# Add GraphQL to server app
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

app.add_route("/graphql", graphql_app)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Raziel death repository",
        version="0.0.1",
        description="This is a custom OpenAPI schema",
        routes=app.routes,
    )
    new_schemas = openapi_schema["components"]["schemas"]
    for i in get_extra_models():
        new_schemas.update(i)
    openapi_schema["components"]["schemas"] = new_schemas

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
