import json
from typing import Dict

from fastapi import APIRouter
from starlette.responses import FileResponse

from managers.graphic_manager import GraphicManager
from managers.predictor_manager import PredictorManager
from repositories.creator import RazielRepoCreator

managersRouter = APIRouter(
    responses={404: {"description": "Not found"}}
)


@managersRouter.post("/deaths-predictor-chart", status_code=200)
def predict_chart_deaths(query: Dict[str, Dict[str, str]] = None, group='ANO', summ='DEFU',
                         period=2):
    predictor = PredictorManager(RazielRepoCreator().factory_method())
    predictor.deaths_forecasting({'query': query}, group, summ, int(period))
    return FileResponse(PredictorManager.CHART_PATH)


@managersRouter.post("/deaths-predictor", status_code=200)
def predict_deaths(query: Dict[str, Dict[str, str]] = None, group='ANO', summ='DEFU', period=2):
    predictor = PredictorManager(RazielRepoCreator().factory_method())
    d = predictor.deaths_forecasting({'query': query}, group, summ, int(period))
    result = d.to_json(orient="split")
    return json.loads(result)


@managersRouter.post("/chart")
def get_chart(query: Dict[str, Dict[str, str]] = None, group='ANO', summ='DEFU'):
    gm = GraphicManager(RazielRepoCreator().factory_method())
    gm.get_chart_by_two_vars({'query': query}, group, summ)
    return FileResponse(GraphicManager.CHART_PATH)
