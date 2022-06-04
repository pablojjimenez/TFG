import json
from typing import Dict

from fastapi import APIRouter
from starlette.responses import FileResponse

from managers.graphic_manager import GraphicManager
from managers.predictor_manager import PredictorManager
from repositories.ccaa_repository import CcaaRepository
from repositories.cie_repository import CieRepository
from repositories.disease_reopsitory import DiseaseRepository
from repositories.gedad_repository import GedadRepository
from repositories.raziel_repository import RazielRepository

managersRouter = APIRouter(
    responses={404: {"description": "Not found"}}
)


@managersRouter.post("/deaths-predictor-chart", status_code=200)
def predict_chart_deaths(query: Dict[str, Dict[str, str]] = None, group='ANO', summ='DEFU',
                         period=2):
    c = RazielRepository(
        'data/raziel',
        DiseaseRepository('data/diseases', CieRepository('data/cie')),
        CcaaRepository('data/ccaas'),
        GedadRepository('data/grupos_edad')
    )
    predictor = PredictorManager(c)
    predictor.deaths_forecasting({'query': query}, group, summ, period)
    return FileResponse(PredictorManager.CHART_PATH)


@managersRouter.post("/deaths-predictor", status_code=200)
def predict_deaths(query: Dict[str, Dict[str, str]] = None, group='ANO', summ='DEFU', period=2):
    c = RazielRepository(
        'data/raziel',
        DiseaseRepository('data/diseases', CieRepository('data/cie')),
        CcaaRepository('data/ccaas'),
        GedadRepository('data/grupos_edad')
    )
    predictor = PredictorManager(c)
    d = predictor.deaths_forecasting({'query': query}, group, summ, period)
    result = d.to_json(orient="split")
    return json.loads(result)


@managersRouter.post("/chart")
def get_chart(query: Dict[str, Dict[str, str]] = None, group='ANO', summ='DEFU'):
    c = RazielRepository(
        'data/raziel',
        DiseaseRepository('data/diseases', CieRepository('data/cie')),
        CcaaRepository('data/ccaas'),
        GedadRepository('data/grupos_edad')
    )
    gm = GraphicManager(c)
    gm.get_chart_by_two_vars({'query': query}, group, summ)
    return FileResponse(GraphicManager.CHART_PATH)
