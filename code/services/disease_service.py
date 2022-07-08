from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from managers.utils import transform_params
from models.exceptions import IncorrectQueryException, DataIsNotAvailable, \
    NoCorrectTypeException, IncorrectColumnNamesException, NoAttributeException
from models.openapi_models.models import MyReturnType, Cie, Gedad, Decease, Ccaa, Disease
from repositories.creator import CcaaRepoCreator, CieRepoCreator, AgesGroupsRepoCreator, \
    DeceaseRepoCreator, DiseaseRepoCreator
from repositories.vars_repository import VarsRepository

dataRouter = APIRouter(
    responses={
        422: {"description": "Unprocessable entity"},
        400: {"description": "Type error in some model fields"},
        500: {"description": "Server internal error"}
    }
)


@dataRouter.post("/diseases", status_code=200, response_model=MyReturnType[Disease])
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
        p = transform_params(query, sort, page, limit)
        objs, tam = DiseaseRepoCreator().get_all_operation(p)
        return {
            'items': objs,
            'length': tam
        }
    except (IncorrectColumnNamesException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvailable:  # pragma: no cover
        raise HTTPException(status_code=505, detail="Data source is not available")


@dataRouter.post("/ccaas", status_code=200, response_model=MyReturnType[Ccaa])
def get_ccaas(query: Dict[str, Dict[str, Any]] = None, sort: str = None,
              page: int = 1, limit: int = 100):
    """
    Get all disease atendiendo al siguiente orden
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    try:
        p = transform_params(query, sort, page, limit)
        objs, tam = CcaaRepoCreator().get_all_operation(p)
        return {
            'items': objs,
            'length': tam
        }
    except (IncorrectColumnNamesException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvailable:  # pragma: no cover
        raise HTTPException(status_code=505, detail="Data source is not available")


@dataRouter.post("/cie", status_code=200, response_model=MyReturnType[Cie])
def get_cies(query: Dict[str, Dict[str, Any]] = None, sort: str = None,
             page: int = 1, limit: int = 100):
    """
    Get all CIE diseases clasification.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    try:
        p = transform_params(query, sort, page, limit)
        objs, tam = CieRepoCreator().get_all_operation(p)
        return {
            'items': objs,
            'length': tam
        }
    except (IncorrectColumnNamesException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvailable:  # pragma: no cover
        raise HTTPException(status_code=505, detail="Data source is not available")


@dataRouter.post("/ages-groups", status_code=200, response_model=MyReturnType[Gedad])
def get_ages_groups(query: Dict[str, Dict[str, Any]] = None, sort: str = None,
                    page: int = 1, limit: int = 100):
    """
    Grupos de edad disponibles para clasificar. Por defecto se devuelven 100 entradas.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    try:
        p = transform_params(None, None, page, limit)
        objs, tam = AgesGroupsRepoCreator().get_all_operation(p)
        return {
            'items': objs,
            'length': tam
        }
    except (IncorrectColumnNamesException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvailable:  # pragma: no cover
        raise HTTPException(status_code=505, detail="Data source is not available")


@dataRouter.post("/deceases", response_model=MyReturnType[Decease])
def get_decease_diseases(query: Dict[str, Dict[str, Any]] = None, sort: str = None,
                         page: int = 1, limit: int = 100):
    """
    Grupos de edad disponibles para clasificar.
    - `sort` propiedad por la que ordenar `'-descripcion'` sentido descendiente
    - `query` formato de la query: `{'def2u': ('>', 5)}`,
    - `page` numero de la pagina solicitada
    - `limit` limnite de elementos
    """
    limit = limit if limit <= 100 else 100
    try:
        p = transform_params(query, sort, page, limit)
        objs, tam = DeceaseRepoCreator().get_all_operation(p)
        return {
            'items': objs,
            'length': tam
        }
    except (IncorrectColumnNamesException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvailable:  # pragma: no cover
        raise HTTPException(status_code=505, detail="Data source is not available")


@dataRouter.get("/vars-meaning", status_code=200, response_model=MyReturnType)
def get_vars_meaning():  # pragma: no cover
    try:
        c = VarsRepository('data/vars')
        objs, tam = c.get_all()
        return {
            'items': objs,
            'length': tam
        }
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvailable:
        raise HTTPException(status_code=505, detail="Data source is not available")
