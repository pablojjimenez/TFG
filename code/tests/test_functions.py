from typing import Dict

from managers.utils import transform_params


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
