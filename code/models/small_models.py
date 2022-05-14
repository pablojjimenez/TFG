from dataclasses import dataclass
from enum import Enum


@dataclass
class Cie:
    id: int
    description: str


@dataclass
class Vars:
    id: str
    description: str


@dataclass
class Ccaa:
    id: str
    name: str


@dataclass
class Gedad:
    id: str
    description: str


class Sex(Enum):
    MALE = 1
    FEMALE = 2
