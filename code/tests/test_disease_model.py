import pytest

from models.disease_model import Disease
from models.exceptions import NoCorrectTypeException
from models.small_models import Cie


class TestDisease:
    def test_should_initialize_object_OK(self):
        data = Disease(id='hola', name='hola', cie=Cie(1, ''))
        assert isinstance(data, Disease)

    def test_should_not_admit_change_cie(self):
        with pytest.raises(NoCorrectTypeException):
            Disease(id='hola', name='hola', cie=10)
