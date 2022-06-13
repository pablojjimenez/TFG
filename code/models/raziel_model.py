from typing import Dict

from models.disease_model import Disease
from models.exceptions import NoAttributeException, NoCorrectTypeException, \
    InvalidIDException
from models.small_models import Ccaa, Gedad


class Raziel(object):
    ALLOW_ATTRS = {
        'ano': int,
        'causa': Disease,
        'sx': int,
        'ccaa': Ccaa,
        'gedad': Gedad,
        'defu': int,
        'avp': int,
        'cruda': float,
        'tavp': float,
        'edad': float,
        'tasae': float,
        'tavpe': float,
        'tasaw': float,
        'tasavpw': float,
        'id': int
    }

    def __init__(self, data: Dict):
        for key in data:
            if key not in self._get_allowed_attrs():
                raise NoAttributeException('Attr is not allowed')
            if not isinstance(data[key], Raziel.ALLOW_ATTRS.get(key)):
                raise NoCorrectTypeException(
                    f'Type: {data[key]} is not {Raziel.ALLOW_ATTRS.get(key)} for {key}'
                )

        self.__dict__.update(data)
        if data.get('id') is not None and data.get('id') > 0:
            self.id = data.get('id')
        else:
            raise InvalidIDException('ID not allowed for Raziel object')

    def _get_allowed_attrs(self):
        return list(map(lambda x: x[0], Raziel.ALLOW_ATTRS.items()))

    def __str__(self) -> str:
        return str(vars(self))
