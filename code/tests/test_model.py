import pytest

from server.disease_model import Disease
from server.raziel_model import Raziel, Sex


class TestModel(object):
    DATA = {'ANO': 0, 'CAUSA': 'str', 'SX': Sex.MEN, 'CCAA': 'str',
                   'GEDAD': 'str', 'DEFU': 9, 'AVP': 9,
                   'CRUDA': 9.9, 'TAVP': 9.9, 'TAVPE': 9.9,
                   'EDAD': 9.9, 'TASAE': 9.9, 'TASAW': 9.9,
                   'TASAVPW': 9.9}

    def test_raziel_model_creation(self):
        Raziel(TestModel.DATA)
        assert True

    def test_raziel_model_bad_creation(self):
        TestModel.DATA['EDAD'] = 'edad'
        with pytest.raises(ValueError):
            Raziel(TestModel.DATA)

    def test_disease_model(self):
        with pytest.raises(ValueError):
            Disease(1, 0)

        assert str(Disease('a', 'o')) == "{'name': 'a', 'cie': 'o'}"
