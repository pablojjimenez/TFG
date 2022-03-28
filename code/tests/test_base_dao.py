import unittest

from tests.base_dao_test import BaseDAOTest


class TestBaseDAO(unittest.TestCase):
    DATA_SIZE = 11

    def setUp(self):
        self.under_test = BaseDAOTest('ages_groups')

    def test_get_all(self):
        data = self.under_test.get_all()
        self.assertEqual(len(data), TestBaseDAO.DATA_SIZE)

    def test_get_one_by_id(self):
        data = self.under_test.get_one_by_id(99)
        self.assertEqual(data[0][2], 'Todas las edades')
        self.assertEqual(data[0][0], 10)

    def test_get_all_sort_id_asc(self):
        params = {
            'sort': 'description'
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), TestBaseDAO.DATA_SIZE)
        self.assertEqual(data[0][1], 1)

    def test_get_all_sort_id_desc(self):
        params = {
            'sort': '-description'
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), TestBaseDAO.DATA_SIZE)
        self.assertEqual(data[0][1], 99)

    def test_get_all_query(self):
        params = {
            'query': 'id=2'
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][2], '5 a 14 años')

    def test_get_all_limit(self):
        params = {
            'limit': 2
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), 2)

    def test_get_all_limit_sort(self):
        params = {
            'limit': 2,
            'sort': '-id'
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0][1], 99)
        self.assertEqual(data[1][1], 10)

    def test_get_all_limit_sort_page_1(self):
        params = {
            'limit': 2,
            'sort': '-id',
            'page': 1
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0][1], 99)
        self.assertEqual(data[1][1], 10)

    def test_get_all_limit_page(self):
        params = {
            'limit': 2,
            'sort': '-id',
            'page': 2
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0][1], 9)
        self.assertEqual(data[1][1], 8)

    def test_get_all_limit_page_2(self):
        params = {
            'limit': 2,
            'sort': '-id',
            'page': 3
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0][1], 7)
        self.assertEqual(data[1][1], 6)

    def test_get_all_limit_page_3(self):
        params = {
            'limit': 3,
            'sort': '-id',
            'page': 3
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0][1], 5)
        self.assertEqual(data[1][1], 4)
        self.assertEqual(data[2][1], 3)

    def test_get_all_limit_page_3_2(self):
        params = {
            'limit': 3,
            'sort': '-id',
            'page': 4
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0][1], 2)
        self.assertEqual(data[1][1], 1)

    def test_get_all_limit_page_query(self):
        params = {
            'limit': 2,
            'sort': '-id',
            'page': 3,
            'query': 'id=1 or id=2'
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), 0)

    def test_get_all_limit_page_query_2(self):
        params = {
            'sort': '-id',
            'query': 'id>1 and id<4'
        }
        data = self.under_test.get_all(params)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0][1], 3)
