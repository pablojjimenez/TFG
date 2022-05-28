import pandas
import pytest

from models.disease_model import Disease
from models.exceptions import NoCorrectColumnsException, IncorrectQueryException
from models.raziel_model import Raziel
from models.small_models import Ccaa, Gedad


class TestRazielRepo:
    def test_get_one_complete_raziel_object(self, mock_raziel_repo):
        obj = mock_raziel_repo.get_all({
            'query': {
                'CRUDA': {
                    '==': '16.694258'
                }
            },
            'page': 1,
            'limit': 1
        })
        obj = obj[0][0]
        assert isinstance(obj, Raziel)
        assert isinstance(obj.ccaa, Ccaa)
        assert isinstance(obj.causa, Disease)
        assert isinstance(obj.gedad, Gedad)

    def test_list_with_param_page1(self, mock_raziel_repo):
        list_param = {
            'page': 1,
            'limit': 5
        }
        obj, tam = mock_raziel_repo.get_all(list_param)
        assert tam == 5
        assert len(obj) == 5
        assert obj[0].id == 1

    def test_list_with_param_page2(self, mock_raziel_repo):
        list_param = {
            'page': 2,
            'limit': 5
        }
        obj, tam = mock_raziel_repo.get_all(list_param)
        assert tam == len(obj)
        assert tam == 5
        assert obj[0].id == 6

    def test_list_with_param_sort(self, mock_raziel_repo):
        list_param = {
            'sort': '-defu',
            'page': 1,
            'limit': 5
        }
        obj, tam = mock_raziel_repo.get_all(list_param)
        assert tam == len(obj)
        assert tam == 5
        assert obj[0].id == 3
        assert obj[0].ano == 1980

    def test_list_with_param_sort2(self, mock_raziel_repo):
        list_param = {
            'sort': 'defu',
            'page': 1,
            'limit': 5
        }
        obj, tam = mock_raziel_repo.get_all(list_param)
        assert tam == len(obj)
        assert tam == 5
        assert obj[0].id == 1

    def test_list_with_query(self, mock_raziel_repo):
        list_param = {
            'query': {'ano': {'==': 1980}, 'CAUSA': {'==': 1}}
        }
        obj, tam = mock_raziel_repo.get_all(list_param)
        assert tam == 6
        for o in obj:
            assert o.ano == 1980

    def test_list_with_all_list_params(self, mock_raziel_repo):
        list_param = {
            'query': {'defu': {'>': 5}},
            'sort': 'cruda',
            'limit': 3,
            'page': 2
        }
        obj, tam = mock_raziel_repo.get_all(list_param)
        assert tam == list_param['limit']
        assert obj[0].id == 15
        assert obj[1].id == 14
        assert obj[2].id == 9

    def test_valid_query_params(self, mock_raziel_repo):
        list_param = {
            'query': {'defu': {'>': 5}},
        }
        _, _ = mock_raziel_repo.get_all(list_param)

    def test_invalid_query_params1(self, mock_raziel_repo):
        list_param = {
            'query': {'def2u': {'>': 5}},
        }
        with pytest.raises(NoCorrectColumnsException):
            mock_raziel_repo.get_all(list_param)

    def test_invalid_query_params2(self, mock_raziel_repo):
        list_param = {
            'query': {'defu': {'o': 5}},
        }
        with pytest.raises(IncorrectQueryException):
            mock_raziel_repo.get_all(list_param)

    def test_prepare_dataframe(self, mock_raziel_repo):
        obj = mock_raziel_repo.prepare_and_grouping_dataframe({}, 'GEDAD', 'DEFU')
        assert isinstance(obj, pandas.DataFrame)

    def test_invalid_vars(self, mock_raziel_repo):
        with pytest.raises(NoCorrectColumnsException):
            mock_raziel_repo.prepare_and_grouping_dataframe({}, 'AAAA', 'B')
