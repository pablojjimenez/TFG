import json
from typing import Dict

from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse

from managers.graphic_manager import GraphicManager
from managers.predictor_manager import PredictorManager
from models.exceptions import DataIsNotAvaible, NoAttributeException, \
    IncorrectColumnNamesException, NoCorrectTypeException
from repositories.creator import DeceaseRepoCreator

managersRouter = APIRouter(
    responses={
        422: {"description": "Unprocessable entity"},
        400: {"description": "Type error in some model fields"},
        500: {"description": "Server internal error"}
    }
)


@managersRouter.post("/deaths-predictor-chart", status_code=201)
def predict_chart_deaths(query: Dict[str, Dict[str, str]] = None, group='ANO', summ='DEFU',
                         period=2):
    try:
        predictor = PredictorManager(DeceaseRepoCreator().factory_method())
        predictor.deaths_forecasting({'query': query}, group, summ, int(period))
        return FileResponse(PredictorManager.CHART_PATH)
    except IncorrectColumnNamesException as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible:
        raise HTTPException(status_code=505, detail="Data source is not available")


@managersRouter.post("/deaths-predictor", status_code=200)
def predict_deaths(query: Dict[str, Dict[str, str]] = None, group='ANO', summ='DEFU', period=2):
    try:
        predictor = PredictorManager(DeceaseRepoCreator().factory_method())
        d = predictor.deaths_forecasting({'query': query}, group, summ, int(period))
        result = d.to_json(orient="split")
        return json.loads(result)
    except IncorrectColumnNamesException as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible:
        raise HTTPException(status_code=505, detail="Data source is not available")


@managersRouter.post("/chart", status_code=201)
def get_chart(query: Dict[str, Dict[str, str]] = None, group='ANO', summ='DEFU'):
    try:
        gm = GraphicManager(DeceaseRepoCreator().factory_method())
        gm.get_chart_by_two_vars({'query': query}, group, summ)
        return FileResponse(GraphicManager.CHART_PATH)
    except IncorrectColumnNamesException as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible:
        raise HTTPException(status_code=505, detail="Data source is not available")
