from typing import Dict

from managers.utils import transform_params
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
        query_str = AbstractRepository.generate_vector_query(query)
        assert query_str == "ID>10 & ID<12 & CIE.isnull()"

    def test_generate_query2(self):
        query = {
            "id": {
                ">": 10,
                "<": 12
            }
        }
        query_str = AbstractRepository.generate_vector_query(query)
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
        query_str = AbstractRepository.generate_vector_query(query)
        assert query_str == "ID>10 & ID<12 & VAR.notnull()"
