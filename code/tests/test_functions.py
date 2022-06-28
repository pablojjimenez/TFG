from typing import Dict

from managers.utils import transform_params, remove_nulls_from_json, change_key_operators
from repositories.abstract_repository import AbstractRepository


class TestAuxFunctions:
    def test_transform_params(self):
        query = None
        sort = 'var'
        page = 1
        limit = 100
        params = transform_params(query, sort, page, limit)
        assert isinstance(params, Dict)
        assert params.get('query', None) is None

    def test_transform_params_query(self):
        query_data = {
            'query': {
                'var': {
                    '==': '100'
                }
            }
        }
        params = transform_params(query_data, None, 1, 100)
        assert params.get('query') == query_data

    def test_generate_query1(self):
        query = {
            "ID": {
                ">": 10,
                "<": 12
            },
            "CIE": {
                "==": ""
            }
        }
        query_str = AbstractRepository.generate_query(query)
        assert query_str == "ID>10 & ID<12 & CIE.isnull()"

    def test_generate_query2(self):
        query = {
            "id": {
                ">": 10,
                "<": 12
            }
        }
        query_str = AbstractRepository.generate_query(query)
        assert query_str == "ID>10 & ID<12"

    def test_generate_query3(self):
        query = {
            "id": {
                ">": 10,
                "<": 12
            },
            "var": {
                '!=': ""
            }
        }
        query_str = AbstractRepository.generate_query(query)
        assert query_str == "ID>10 & ID<12 & VAR.notnull()"

    def test_generate_query_like(self):
        query = {
            "id": {
                ">": 10
            },
            "var": {
                'like': "?lgo"
            },
            "var2": {
                '!=': ""
            }
        }
        query_str = AbstractRepository.generate_query(query)
        assert query_str == 'ID>10 & VAR.str.contains("?lgo", na=False) & VAR2.notnull()'

    def test_generate_query_like_with_lists(self):
        query = {
            "var": {
                'like': "?lgo"
            },
            "id": {
                "==": [10, 11, 12]
            }
        }
        query_str = AbstractRepository.generate_query(query)
        assert query_str == 'VAR.str.contains("?lgo", na=False) & ID==10 | ID==11 | ID==12'

    def test_generate_query_like_with_lists_str(self):
        query = {
            "id": {
                "==": ["hola", "adios"]
            }
        }
        query_str = AbstractRepository.generate_query(query)
        assert query_str == "ID=='hola' | ID=='adios'"

    def test_remove_nulls_from_json1(self):
        data = {'id': {'eq': 1, 'gt': None, 'lt': None}, 'name': None}
        rtado = remove_nulls_from_json(data)
        assert rtado == {'id': {'eq': 1}}

    def test_remove_nulls_from_json2(self):
        data = {'id': {'eq': 1, 'gt': None, 'lt': None, 'other': {'a': None}},
                'name': None, 'ab': None}
        rtado = remove_nulls_from_json(data)
        assert rtado == {'id': {'eq': 1}}

    def test_remove_nulls_from_json3(self):
        data = {'id': {'eq': 1, 'gt': None, 'lt': None}, 'name': None, 'ab': None,
                'id1': {'eq': None, 'gt': None, 'lt': None}}
        rtado = remove_nulls_from_json(data)
        assert rtado == {'id': {'eq': 1}}

    def test_remove_nulls_from_json4(self):
        data = {'id': {'eq': 1, 'gt': None, 'lt': None}, 'name': None, 'ab': None,
                'id1': {'eq': None, 'gt': None, 'lt': {'c': 2}}}
        rtado = remove_nulls_from_json(data)
        assert rtado == {'id': {'eq': 1}, 'id1': {'lt': {'c': 2}}}

    def test_remove_nulls_from_json5(self):
        data = {'id': {'eq': 1, 'gt': None, 'lt': None, 'neq': None}, 'name': None, 'ab': None,
                'id1': {'eq': None, 'gt': None, 'lt': {'c': 2}}}
        rtado = remove_nulls_from_json(data)
        assert rtado == {'id': {'eq': 1, 'neq': None}, 'id1': {'lt': {'c': 2}}}

    def test_remove_nulls_from_json6(self):
        data = {'id': {'eq': 1, 'gt': None, 'lt': None}, 'name': None, 'ab': None,
                'id1': {'eq': None, 'gt': None, 'lt': {'c': 2}}, 'id2': {'neq': None}}
        rtado = remove_nulls_from_json(data)
        assert rtado == {'id': {'eq': 1}, 'id1': {'lt': {'c': 2}}, 'id2': {'neq': None}}

    def test_change_keys_operators(self):
        data = {'id': {'eq': 1}, 'id1': {'lt': 2}}
        rtado = change_key_operators(data)
        assert rtado == {'id': {'==': 1}, 'id1': {'<': 2}}

    def test_change_keys_operators2(self):
        data = {'id': {'eq': 1}, 'bb': {'gt': 3}, 'cc': {'lt': 9}}
        rtado = change_key_operators(data)
        assert rtado == {'id': {'==': 1}, 'bb': {'>': 3}, 'cc': {'<': 9}}

    '''
    TODO: when the new tests changes are merged
    def test_get_diseases_based_on_cies(self):
        filter_obj = DiseasesSearchFilter(id=None, diseaseName='a', cieName='a')
        diseases = Mutation.get_diseases_based_on_cies(filter_obj, None, 1, 10)
        assert len(diseases) == 3
    '''
