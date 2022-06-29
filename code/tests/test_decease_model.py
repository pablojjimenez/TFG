import pytest

from models.disease_model import Disease
from models.exceptions import NoAttributeException, NoCorrectTypeException, InvalidIDException
from models.decease_model import Decease
from models.small_models import Cie, Sex, Ccaa, Gedad


class TestDecease:
    JSON_DATA = {
        'ano': 2020,
        'causa': Disease(2, 'reason', Cie(1, '')),
        'sexo': Sex.FEMALE,
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

    def test_should_create_Decease_with_all_field_none(self):
        with pytest.raises(NoAttributeException):
            Decease({'attr_random': 23})

    def test_create_correct_Decease_object_from_json(self):
        TestDecease.JSON_DATA['id'] = 7
        decease = Decease(TestDecease.JSON_DATA)
        assert isinstance(decease, Decease)

    def test_create_incorrect_decease_object_from_json(self):
        with pytest.raises(NoCorrectTypeException):
            data = TestDecease.JSON_DATA.copy()
            data['gedad'] = 2
            Decease(data)

    def test_create_incorrect_id(self):
        with pytest.raises(InvalidIDException):
            TestDecease.JSON_DATA['id'] = -1
            Decease(TestDecease.JSON_DATA)
