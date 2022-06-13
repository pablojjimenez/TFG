import pytest

from models.disease_model import Disease
from models.exceptions import NoAttributeException, NoCorrectTypeException
from models.raziel_model import Raziel
from models.small_models import Cie, Ccaa, Gedad


class TestRaziel:
    JSON_DATA = {
        'ano': 2020,
        'causa': Disease(2, 'reason', Cie(1, '')),
        'sexo': 1,
        'ccaa': Ccaa(1, ''),
        'gedad': Gedad(1, ''),
        'defu': 0,
        'avp': 0,
        'cruda': 0.0,
        'tavp': 0.0,
        'edad': 2.9,
        'tasae': 0.0,
        'tavpe': 0.0,
        'tasaw': 0.0,
        'tasavpw': 0.0
    }

    def test_should_create_Raziel_with_all_field_none(self):
        with pytest.raises(NoAttributeException):
            Raziel({'attr_random': 23})

    def test_create_correct_raziel_object_from_json(self):
        TestRaziel.JSON_DATA['id'] = 7
        raziel = Raziel(TestRaziel.JSON_DATA)
        assert isinstance(raziel, Raziel)

    def test_create_incorrect_raziel_object_from_json(self):
        with pytest.raises(NoCorrectTypeException):
            TestRaziel.JSON_DATA['gedad'] = 2
            Raziel(TestRaziel.JSON_DATA)
