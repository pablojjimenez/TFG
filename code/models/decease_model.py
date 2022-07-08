from typing import Dict

from models.disease_model import Disease
from models.exceptions import NoAttributeException, NoCorrectTypeException, \
    InvalidIDException
from models.small_models import Sex, Ccaa, Gedad


class Decease(object):
    """
    Description:
        Raziel is the abstraction of the data stored in the raziel CSV. This class
        represent the deaths associated with the population on a disease, also provides some
        types and constraint validation. Its properties are all the data stored by the ISCIII
    Properties:
        ano: int - year of the data
        causa: Disease - disease object
        sx: int - gender of the person (1: man, 2: woman)
        ccaa: Ccaa - Spanish state object
        gedad: Gedad - age group at death
        defu: int - number of deaths
        avp: int - potential years of life lost
        cruda: float - crude rate
        tavp: float - rate of potential years of life lost
        edad: float - average age at death
        tasae: float - adjusted rate for the European population
        tavpe: float - adjusted rate of years of potential life lost
        tasaw: float - adjusted rate for the world population
        tasavpw: float - adjusted rate of potential years of life lost
        id: int - Internal row identification
    """
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
                raise NoAttributeException(f'{key} Attr is not allowed')
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
