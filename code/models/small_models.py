from dataclasses import dataclass
from enum import Enum


@dataclass
class Cie:
    """
    This is the acronym for the International
    Classification of Diseases, 10th edition.
    """
    id: int
    name: str


@dataclass
class Vars:
    """
    Generic classification variables
    """
    id: str
    description: str


@dataclass
class Ccaa:
    """
    Represents the states of Spain.
    """
    id: str
    name: str


@dataclass
class Gedad:
    """
    Represents the age groups
    """
    id: str
    description: str


class Sex(Enum):
    MALE = 1
    FEMALE = 2
