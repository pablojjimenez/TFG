import json
from typing import Dict

from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse

from managers.graphic_manager import GraphicManager
from managers.predictor_manager import PredictorManager
from models.exceptions import DataIsNotAvailable, NoAttributeException, \
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
        if query is None:
            raise HTTPException(status_code=400, detail="Body param is mandatory")
        predictor = PredictorManager(DeceaseRepoCreator().factory_method())
        _, img_path = predictor.deaths_forecasting({'query': query}, group, summ, int(period))
        return FileResponse(img_path)
    except IncorrectColumnNamesException as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvailable:  # pragma: no cover
        raise HTTPException(status_code=505, detail="Data source is not available")


@managersRouter.post("/deaths-predictor", status_code=200)
def predict_deaths(query: Dict[str, Dict[str, str]] = None, group='ANO', summ='DEFU', period=2):
    try:
        if query is None:
            raise HTTPException(status_code=400, detail="Body param is mandatory")
        predictor = PredictorManager(DeceaseRepoCreator().factory_method())
        d, _ = predictor.deaths_forecasting({'query': query}, group, summ, int(period))
        result = d.to_json(orient="split")
        return json.loads(result)
    except IncorrectColumnNamesException as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvailable:  # pragma: no cover
        raise HTTPException(status_code=505, detail="Data source is not available")


@managersRouter.post("/chart", status_code=201)
def get_chart(query: Dict[str, Dict[str, str]] = None, group='ANO', summ='DEFU'):
    try:
        gm = GraphicManager(DeceaseRepoCreator().factory_method())
        img = gm.get_chart_by_two_vars({'query': query}, group, summ)
        return FileResponse(img)
    except IncorrectColumnNamesException as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvailable:  # pragma: no cover
        raise HTTPException(status_code=505, detail="Data source is not available")
