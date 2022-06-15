from fastapi import APIRouter, HTTPException
from typing import Dict

from managers.utils import call_repository_get_all
from models.exceptions import IncorrectQueryException, NoCorrectColumnsException, DataIsNotAvaible, \
    NoCorrectTypeException, NoAttributeException
from repositories.ccaa_repository import CcaaRepository
from repositories.cie_repository import CieRepository
from repositories.disease_repository import DiseaseRepository
from repositories.gedad_repository import GedadRepository
from repositories.raziel_repository import RazielRepository
from repositories.vars_repository import VarsRepository

dataRouter = APIRouter(
    responses={
        422: {"description": "Unprocessable entity"},
        400: {"description": "Type error in some model fields"},
        500: {"description": "Server internal error"}
    }
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
    try:
        return call_repository_get_all(
            DiseaseRepository('data/diseases', CieRepository('data/cie')),
            query, sort, page, limit
        )
    except (NoCorrectColumnsException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible as _:
        raise HTTPException(status_code=505, detail="Data source is not available")


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
    try:
        return call_repository_get_all(
            CcaaRepository('data/ccaas'),
            query, sort, page, limit
        )
    except (NoCorrectColumnsException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible as _:
        raise HTTPException(status_code=505, detail="Data source is not available")


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
    try:
        return call_repository_get_all(
            CieRepository('data/cie'),
            query, sort, page, limit
        )
    except (NoCorrectColumnsException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible as _:
        raise HTTPException(status_code=505, detail="Data source is not available")


@dataRouter.post("/ages-groups")
def get_ages_groups(page: int = 1, limit: int = 100):
    """
    Grupos de edad disponibles para clasificar. Por defecto se devuelven 100 entradas.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    try:
        return call_repository_get_all(
            GedadRepository('data/grupos_edad'),
            None, None, page, limit
        )
    except (NoCorrectColumnsException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible as _:
        raise HTTPException(status_code=505, detail="Data source is not available")


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
    try:
        return call_repository_get_all(
            RazielRepository(
                'data/raziel',
                DiseaseRepository('data/diseases', CieRepository('data/cie')),
                CcaaRepository('data/ccaas'),
                GedadRepository('data/grupos_edad')
            ),
            query, sort, page, limit
        )
    except (NoCorrectColumnsException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible as _:
        raise HTTPException(status_code=505, detail="Data source is not available")


@dataRouter.get("/vars-meaning")
def get_vars_meaning():
    try:
        c = VarsRepository('data/vars')
        objs, tam = c.get_all()
        return {
            'items': objs,
            'length': tam
        }
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible as _:
        raise HTTPException(status_code=505, detail="Data source is not available")
