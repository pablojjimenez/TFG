import pytest

from server.raziel_model import Raziel


class MyTestCase(object):
    DATA = {
        'id': 1,
        'ANO': 2022,
        'CAUSA': 'causa 1',
        'SX': 'Femenino',
        'CCAA': 'Andalucía',
        'GEDAD': 'de 5 a 10 años',
        'DEFU': 59,
        'AVP': 0,
        'CRUDA': 0,
        'TAVP': 0,
        'EDAD': 2.5,
        'TASAE': 0,
        'TASAW': 0,
        'TASAVPW': 0
    }

    def test_raziel_model_creation(self):
        MyTestCase.DATA['TAVPE'] = 0
        Raziel(MyTestCase.DATA)
        assert True == True

    def test_raziel_model_bad_creation(self):
        with pytest.raises(ValueError):
            Raziel(MyTestCase.DATA)
