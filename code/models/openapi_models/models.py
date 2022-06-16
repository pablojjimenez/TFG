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


class Raziel(BaseModel):
    ano: int = Field(description="año de consulta (1980-2020)")
    causa: Disease = Field(description="Causa")
    sexo: Sex = Field(description="Sexo")
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
