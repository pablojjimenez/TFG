import pytest

from models.disease_model import Disease
from models.exceptions import DataIsNotAvailable
from models.small_models import Cie
from repositories.disease_repository import DiseaseRepository


class TestDiseaseRepo:
    def test_create_reopsitory_from_blank_directory(self):
        with pytest.raises(DataIsNotAvailable):
            DiseaseRepository('directory/fake', None)

    def test_get_one_uncomplete_disease_object(self, mock_disease):
        obj = mock_disease.get_one(2)
        assert isinstance(obj, Disease)
        assert obj.cie is None

    def test_get_one_complete_disease_object(self, mock_disease):
        obj = mock_disease.get_one(1)
        assert isinstance(obj, Disease)
        assert isinstance(obj.cie, Cie)

    def test_two_queries_over_same_var(self, mock_disease):
        list_param = {
            'query': {'id': {'>': 1, '<': 3}}
        }
        _, tam = mock_disease.get_all(list_param)
        assert tam == 1
