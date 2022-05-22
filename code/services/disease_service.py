from json import JSONDecodeError
from fastapi import APIRouter, HTTPException
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from typing import Union, Dict

from managers.utils import transform_params
from repositories.ccaa_repository import CcaaRepository
from repositories.cie_repository import CieRepository
from repositories.disease_reopsitory import DiseaseRepository
from repositories.gedad_repository import GedadRepository
from repositories.raziel_repository import RazielRepository
from repositories.vars_repository import VarsRepository

dataRouter = APIRouter(
    responses={404: {"description": "Not found"}}
)

class QueryModel(BaseModel):
    query: Union[Dict[str, str], None]

@dataRouter.get("/diseases", status_code=200)
def get_diseases(query: QueryModel = None, sort: str = None, page: int = None, limit: int = None):
    """
    Get all disease atendiendo al siguiente orden
    - `sort` propiedad por la que ordenar `'-propiedad'` sentido descendiente
    - `query` formato de la query: `{'defu': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = DiseaseRepository('data/diseases', CieRepository('data/cie'))
    
    try:
        print(query)
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail=str(e))

    objs, tam = c.get_all(p)
    return {
        'items': objs,
        'length': tam
    }


@dataRouter.get("/ccaas")
def get_ccaas(sort: str = None, query: str = None, page: int = None, limit: int = None):
    """
    Get all disease atendiendo al siguiente orden
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = CcaaRepository('data/ccaas')

    try:
        p = transform_params(sort, query, page, limit)
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail='Bad syntax for query json')
    

    objs, tam = c.get_all(p)
    return {
        'items': objs,
        'length': tam
    }


@dataRouter.get("/cie")
def get_cies(sort: str = None, query: str = None, page: int = None, limit: int = None):
    """
    Get all CIE diseases clasification.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = CieRepository('data/cie')

    try:
        p = transform_params(sort, query, page, limit)
        objs, tam = c.get_all(p)
    except (JSONDecodeError, Exception):
        raise HTTPException(status_code=400, detail='Bad syntax for query json')

    return {
        'items': objs,
        'length': tam
    }


@dataRouter.get("/cie")
def get_cies(sort: str = None, query: str = None, page: int = 1, limit: int = 100):
    """
    Get all CIE diseases clasification.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = CieRepository('data/cie')
    try:
        p = transform_params(sort, query, page, limit)
    except JSONDecodeError or Exception:
        raise HTTPException(status_code=400, detail='Bad syntax for query json')
    
    objs, tam = c.get_all(p)
    return {
        'items': objs,
        'length': tam
    }


@dataRouter.get("/ages-groups")
def get_ages_groups(sort: str = None, query: str = None, page: int = None, limit: int = None):
    """
    Grupos de edad disponibles para clasificar. Por defecto se devuelven 100 entradas.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    c = GedadRepository('data/grupos_edad')
    try:
        p = transform_params(sort, query, page, limit)
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail='Bad syntax for query json')
    
    objs, tam = c.get_all(p)
    return {
        'items': objs,
        'length': tam
    }


@dataRouter.get("/raziel")
def get_raziel_diseases(sort: str = None, query: str = None, page: int = 1, limit: int = 100):
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
        p = transform_params(sort, query, page, limit)
    except JSONDecodeError or Exception:
        raise HTTPException(status_code=400, detail='Bad syntax for query json')
    
    objs, tam = c.get_all(p)
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
