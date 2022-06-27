import strawberry
import typing

from dataclasses import asdict

T = typing.TypeVar("T")


@strawberry.type
class CcaaDTO:
    id: str
    name: str


@strawberry.type
class CieDTO:
    id: str
    name: str


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
class DeceaseDTO:
    ano: int
    causa: DiseaseDTO
    sx: int
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
class MyReturnType(typing.Generic[T]):
    items: typing.List[T]
    length: int


@strawberry.input
class FilterOperators(typing.Generic[T]):
    eq: typing.Optional[T] = None
    gt: typing.Optional[T] = None
    lt: typing.Optional[T] = None
    neq: typing.Optional[T] = None
    like: typing.Optional[T] = None


class Filter:
    def dict_repr(self) -> dict:
        return {k: v for k, v in asdict(self).items() if self.__dataclass_fields__[k].repr}


@strawberry.input
class DiseasesFilter(Filter):
    id: typing.Optional[FilterOperators[int]] = None
    name: typing.Optional[FilterOperators[str]] = None
    cie: typing.Optional[FilterOperators[str]] = None


@strawberry.input
class DiseasesSearchFilter(Filter):
    id: typing.Optional[str] = None
    diseaseName: typing.Optional[str] = None
    cieName: typing.Optional[str] = None


@strawberry.input
class DeceaseFilter(Filter):
    id: typing.Optional[FilterOperators[int]] = None
    ano: typing.Optional[FilterOperators[int]] = None
    causa: typing.Optional[FilterOperators[int]] = None
    sx: typing.Optional[FilterOperators[float]] = None
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
