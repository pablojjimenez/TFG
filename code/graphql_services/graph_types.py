import typing
import strawberry

from dataclasses import asdict
from typing import Generic

from repositories.ccaa_repository import CcaaRepository
from repositories.cie_repository import CieRepository
from repositories.disease_reopsitory import DiseaseRepository
from repositories.gedad_repository import GedadRepository

T = typing.TypeVar("T")


@strawberry.type
class CcaaDTO:
    id: str
    name: str


@strawberry.type
class CieDTO:
    id: str
    description: str


@strawberry.type
class DiseaseDTO:
    id: str
    name: str
    cie: typing.Optional[CieDTO]


@strawberry.type
class GedadDTO:
    id: str
    description: str


@strawberry.type
class RazielDTO:
    ano: int
    causa: DiseaseDTO
    sexo: int
    ccaa: CcaaDTO
    gedad: GedadDTO
    defu: int
    avp: int
    cruda: float
    tavp: float
    edad: float
    tasae: float
    tavpe: float
    tasaw: float
    tasavpw: float
    id: int


@strawberry.type
class MyReturnType(Generic[T]):
    items: typing.List[T]
    length: int


def get_ccaas():
    rtado = CcaaRepository('data/ccaas').get_all()
    return MyReturnType[CcaaDTO](rtado[0], rtado[1])


def get_cies():
    rtado = CieRepository('data/cie').get_all()
    return MyReturnType[CieDTO](rtado[0], rtado[1])


def get_diseases():
    rtado = DiseaseRepository('data/diseases', CieRepository('data/cie')).get_all()
    return MyReturnType[DiseaseDTO](rtado[0], rtado[1])


def get_ages_groups():
    rtado = GedadRepository('data/grupos_edad').get_all()
    return MyReturnType[GedadDTO](rtado[0], rtado[1])


@strawberry.type
class Query:
    ccaas: MyReturnType[CcaaDTO] = strawberry.field(resolver=get_ccaas)
    cies: MyReturnType[CieDTO] = strawberry.field(resolver=get_cies)
    diseases: MyReturnType[DiseaseDTO] = strawberry.field(resolver=get_diseases)
    ages_groups: MyReturnType[GedadDTO] = strawberry.field(resolver=get_ages_groups)


@strawberry.type
class MyQuery:
    query: typing.Dict


@strawberry.input
class FilterOperators(Generic[T]):
    eq: typing.Optional[T] = None
    gt: typing.Optional[T] = None
    lt: typing.Optional[T] = None
    neq: typing.Optional[T] = None


class Filter:
    def dict_repr(self) -> dict:
        return {k: v for k, v in asdict(self).items() if self.__dataclass_fields__[k].repr}


@strawberry.input
class CCAAFilter(Filter):
    id: typing.Optional[FilterOperators[int]] = None
    name: typing.Optional[FilterOperators[str]] = None


@strawberry.input
class DiseasesFilter(Filter):
    id: typing.Optional[FilterOperators[int]] = None
    name: typing.Optional[FilterOperators[str]] = None
    cie: typing.Optional[FilterOperators[str]] = None


@strawberry.input
class RazielFilter(Filter):
    id: typing.Optional[FilterOperators[int]] = None
    ano: typing.Optional[FilterOperators[int]] = None
    causa: typing.Optional[DiseasesFilter] = None
    sexo: typing.Optional[FilterOperators[float]] = None
    ccaa: typing.Optional[FilterOperators[int]] = None
    gedad: typing.Optional[FilterOperators[int]] = None
    defu: typing.Optional[FilterOperators[int]] = None
    avp: typing.Optional[FilterOperators[int]] = None
    cruda: typing.Optional[FilterOperators[float]] = None
    tavp: typing.Optional[FilterOperators[float]] = None
    edad: typing.Optional[FilterOperators[float]] = None
    tasae: typing.Optional[FilterOperators[float]] = None
    tavpe: typing.Optional[FilterOperators[float]] = None
    tasaw: typing.Optional[FilterOperators[float]] = None
    tasavpw: typing.Optional[FilterOperators[float]] = None
