import strawberry
from fastapi import FastAPI

from starlette.requests import Request
from fastapi.exceptions import HTTPException
from starlette.responses import Response, JSONResponse
from strawberry.asgi import GraphQL

from graphql_services.graph_types import Query
from graphql_services.graphql_mutation import Mutation
from services.disease_service import dataRouter
from services.managers_service import managersRouter


class validation_exception_handler:
    def __call__(self, request: Request, ex: Exception) -> Response:
        return JSONResponse(
            {
                "error_message": ex.detail,
                "code": 400
            }, status_code=400)


# Create FastAPI app
app = FastAPI()
app.include_router(dataRouter, tags=["Api resources"], prefix="/data")
app.include_router(managersRouter, tags=["Api managers"], prefix="/managers")
app.add_exception_handler(HTTPException, validation_exception_handler())

# Add GraphQL to server app
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

app.add_route("/graphql", graphql_app)
#app.add_websocket_route("/graphql_services", graphql_app)
