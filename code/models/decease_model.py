from typing import Dict

from models.disease_model import Disease
from models.exceptions import NoAttributeException, NoCorrectTypeException, \
    InvalidIDException
from models.small_models import Sex, Ccaa, Gedad


class Decease(object):
    ALLOW_ATTRS = {
        'ano': int,
        'causa': Disease,
        'sexo': Sex,
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
            if not isinstance(data[key], Decease.ALLOW_ATTRS.get(key)):
                raise NoCorrectTypeException(
                    f'Type: {data[key]} is not {Decease.ALLOW_ATTRS.get(key)} for {key}'
                )

        self.__dict__.update(data)
        if data.get('id') is not None and data.get('id') > 0:
            self.id = data.get('id')
        else:
            raise InvalidIDException('ID not allowed for Decease object')

    def _get_allowed_attrs(self):
        return list(map(lambda x: x[0], Decease.ALLOW_ATTRS.items()))

    def __str__(self) -> str:
        return str(vars(self))
