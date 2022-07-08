from typing import Union, List
from typing import Generic

import typing
from pydantic import BaseModel, Field

from models.small_models import Sex


class Cie(BaseModel):
    id: int = Field(...)
    description: str = Field(...)


class Vars(BaseModel):
    id: str = Field(...)
    description: str = Field(...)


class Ccaa(BaseModel):
    id: str = Field(...)
    name: str = Field(...)


class Gedad(BaseModel):
    id: str = Field(...)
    description: str = Field(...)


class Disease(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    cie: Union[Cie, None] = Field(...)


class Decease(BaseModel):
    ano: int = Field(description="año de consulta (1980-2020)")
    causa: Disease = Field(description="Causa")
    sx: int = Field(description="Sexo")
    ccaa: Ccaa = Field(description="Comunidad Autónoma")
    gedad: Gedad = Field(description="Grupos de edad")
    defu: int = Field(description="Número de defunciones")
    avp: int = Field(description="Años potenciales de vida perdidos")
    cruda: float = Field(description="Tasa bruta")
    tavp: float = Field(description="Tasa de años potenciales de vida perdidos")
    edad: float = Field(description="Edad media a la defunción")
    tasae: float = Field(description="Tasa ajustada a la población europea")
    tavpe: float = Field(description="Tasa ajustada de años potenciales de vida perdidos ")
    tasaw: float = Field(description="Tasa ajustada a la población mundial")
    tasavpw: float = Field(description="Tasa ajustada de años potenciales de vida perdidos")
    id: int = Field(...)


T = typing.TypeVar("T")


class MyReturnType(BaseModel, Generic[T]):
    items: List[T] = Field(...)
    length: int = Field(...)


def get_extra_models():
    return [
        {
            "Cie": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "int",
                    },
                    "description": {
                        "type": "str",
                    }
                }
            }
        },
        {
            "Ccaa": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "int",
                    },
                    "name": {
                        "type": "str",
                    }
                }
            }
        },
        {
            "Gedad": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "int",
                    },
                    "description": {
                        "type": "str",
                    }
                }
            }
        },
        {
            "Disease": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "int",
                    },
                    "name": {
                        "type": "str",
                    },
                    "cie": {
                        "type": "Cie object"
                    }
                }
            }
        },
        {
            "Decease": {
                "type": "object",
                "properties": {
                    "ano": {
                        "type": "int",
                    },
                    "causa": {
                        "type": "Disease object"
                    },
                    "sx": {
                        "type": "int in [1, 2]",
                    },
                    "ccaa": {
                        "type": "Ccaa object",
                    },
                    "gedad": {
                        "type": "Gedad object",
                    },
                    "defu": {
                        "type": "int",
                    },
                    "avp": {
                        "type": "int",
                    },
                    "cruda": {
                        "type": "float",
                    },
                    "tavp": {
                        "type": "float",
                    },
                    "edad": {
                        "type": "float",
                    },
                    "tasae": {
                        "type": "float",
                    },
                    "tavpe": {
                        "type": "float",
                    },
                    "tasaw": {
                        "type": "float",
                    },
                    "tasavpw": {
                        "type": "float",
                    }
                }
            }
        },
    ]
