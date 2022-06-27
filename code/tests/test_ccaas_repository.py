from models.small_models import Ccaa


class TestCcaaRepository:

    def test_get_all_ccaas(self, mock_ccaas):
        ccaas = mock_ccaas.get_all({'limit': 1, 'page': 1})
        assert ccaas[1] == 1
        assert isinstance(ccaas[0][0], Ccaa)
