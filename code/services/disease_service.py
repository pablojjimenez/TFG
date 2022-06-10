from fastapi import APIRouter, HTTPException
from typing import Dict

from managers.utils import transform_params
from models.exceptions import IncorrectQueryException, NoCorrectColumnsException
from repositories.ccaa_repository import CcaaRepository
from repositories.cie_repository import CieRepository
from repositories.disease_reopsitory import DiseaseRepository
from repositories.gedad_repository import GedadRepository
from repositories.raziel_repository import RazielRepository
from repositories.vars_repository import VarsRepository

dataRouter = APIRouter(
    responses={404: {"description": "Not found"}}
)


@dataRouter.post("/diseases", status_code=200)
def get_diseases(query: Dict[str, Dict[str, str]] = None, sort: str = None,
                 page: int = 1, limit: int = 100):
    """
    Get all disease atendiendo al siguiente orden
    - `sort` propiedad por la que ordenar `'-propiedad'` sentido descendiente
    - `query` formato de la query: `{'defu': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = DiseaseRepository('data/diseases', CieRepository('data/cie'))

    try:
        p = transform_params(query, sort, page, limit)
        objs, tam = c.get_all(p)
    except (NoCorrectColumnsException, IncorrectQueryException, Exception) as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        'items': objs,
        'length': tam
    }


@dataRouter.post("/ccaas")
def get_ccaas(query: Dict[str, Dict[str, str]] = None, sort: str = None,
              page: int = 1, limit: int = 100):
    """
    Get all disease atendiendo al siguiente orden
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = CcaaRepository('data/ccaas')

    try:
        p = transform_params(query, sort, page, limit)
        objs, tam = c.get_all(p)
    except (NoCorrectColumnsException, IncorrectQueryException, Exception) as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        'items': objs,
        'length': tam
    }


@dataRouter.post("/cie")
def get_cies(query: Dict[str, Dict[str, str]] = None, sort: str = None,
             page: int = 1, limit: int = 100):
    """
    Get all CIE diseases clasification.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = CieRepository('data/cie')

    try:
        p = transform_params(query, sort, page, limit)
        objs, tam = c.get_all(p)
    except (NoCorrectColumnsException, IncorrectQueryException, Exception) as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        'items': objs,
        'length': tam
    }


@dataRouter.post("/ages-groups")
def get_ages_groups(query: Dict[str, Dict[str, str]] = None, sort: str = None,
                    page: int = 1, limit: int = 100):
    """
    Grupos de edad disponibles para clasificar. Por defecto se devuelven 100 entradas.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = GedadRepository('data/grupos_edad')

    try:
        p = transform_params(query, sort, page, limit)
        objs, tam = c.get_all(p)
    except (NoCorrectColumnsException, IncorrectQueryException, Exception) as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        'items': objs,
        'length': tam
    }


@dataRouter.post("/raziel")
def get_raziel_diseases(query: Dict[str, Dict[str, str]] = None, sort: str = None,
                        page: int = 1, limit: int = 100):
    """
    Grupos de edad disponibles para clasificar.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = RazielRepository(
        'data/raziel',
        DiseaseRepository('data/diseases', CieRepository('data/cie')),
        CcaaRepository('data/ccaas'),
        GedadRepository('data/grupos_edad')
    )

    try:
        p = transform_params(query, sort, page, limit)
        objs, tam = c.get_all(p)
    except (NoCorrectColumnsException, IncorrectQueryException, Exception) as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        'items': objs,
        'length': tam
    }


@dataRouter.get("/vars-meaning")
def get_vars_meaning():
    c = VarsRepository('data/vars')
    objs, tam = c.get_all()
    return {
        'items': objs,
        'length': tam
    }
