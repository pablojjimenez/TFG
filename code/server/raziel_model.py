from enum import Enum
from typing import Dict

from server.base_model import MyModel


class Sex(Enum):
    MEN = 1
    WOMEN = 2


class Raziel(MyModel):
    ALLOW_ATTRS = {'ANO': int, 'CAUSA': str, 'SX': Sex, 'CCAA': str,
                   'GEDAD': str, 'DEFU': int, 'AVP': int,
                   'CRUDA': float, 'TAVP': float, 'TAVPE': float,
                   'EDAD': float, 'TASAE': float, 'TASAW': float,
                   'TASAVPW': float}

    def __init__(self, data: Dict):
        for key in data:
            if key not in self._get_allowed_attrs():
                raise ValueError('Attr is not allowed')
            if not isinstance(data[key], Raziel.ALLOW_ATTRS.get(key)):
                raise ValueError('Attr type is not allowed')

        super().__init__(data)

    def _get_allowed_attrs(self):
        return list(map(lambda x: x[0], Raziel.ALLOW_ATTRS.items()))

    def _fill(self, data: Dict):
        super()._fill_attrs(data)
