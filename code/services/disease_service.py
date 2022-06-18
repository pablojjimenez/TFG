from fastapi import APIRouter, HTTPException
from typing import Dict

from managers.utils import transform_params
from models.exceptions import IncorrectQueryException, NoCorrectColumnsException, \
    NoCorrectTypeException, DataIsNotAvaible, NoAttributeException
from repositories.creator import CcaaRepoCreator, CieRepoCreator, AgesGroupsRepoCreator, \
    RazielRepoCreator, DiseaseRepoCreator
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
        p = transform_params(query, sort, page, limit)
        objs, tam = DiseaseRepoCreator().get_all_operation(p)
        return {
            'items': objs,
            'length': tam
        }
    except (NoCorrectColumnsException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible:
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
        p = transform_params(query, sort, page, limit)
        objs, tam = CcaaRepoCreator().get_all_operation(p)
        return {
            'items': objs,
            'length': tam
        }
    except (NoCorrectColumnsException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible:
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
        p = transform_params(query, sort, page, limit)
        objs, tam = CieRepoCreator().get_all_operation(p)
        return {
            'items': objs,
            'length': tam
        }
    except (NoCorrectColumnsException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible:
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
        p = transform_params(None, None, page, limit)
        objs, tam = AgesGroupsRepoCreator().get_all_operation(p)
        return {
            'items': objs,
            'length': tam
        }
    except (NoCorrectColumnsException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible:
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
        p = transform_params(query, sort, page, limit)
        objs, tam = RazielRepoCreator().get_all_operation(p)
        return {
            'items': objs,
            'length': tam
        }
    except (NoCorrectColumnsException, IncorrectQueryException) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (NoCorrectTypeException, NoAttributeException, ValueError) as e2:
        raise HTTPException(status_code=400, detail=str(e2))
    except DataIsNotAvaible:
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
    except DataIsNotAvaible:
        raise HTTPException(status_code=505, detail="Data source is not available")
