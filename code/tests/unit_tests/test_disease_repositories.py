from models.disease_model import Disease
from models.small_models import Cie


class TestDiseaseRepo:
    def test_get_one_uncomplete_disease_object(self, mock_disease):
        obj = mock_disease.get_one(2)
        assert isinstance(obj, Disease)
        assert obj.cie is None

    def test_get_one_complete_disease_object(self, mock_disease):
        obj = mock_disease.get_one(1)
        assert isinstance(obj, Disease)
        assert isinstance(obj.cie, Cie)
