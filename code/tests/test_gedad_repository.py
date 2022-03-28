import unittest

from models.small_models import Gedad
from repositories.gedad_repository import GedadRepository
from tests.base_dao_test import BaseDAOTest


class TestGedadRepository(unittest.TestCase):
    DATA_SIZE = 11

    def setUp(self):
        self.under_test = GedadRepository(BaseDAOTest('ages_groups'))

    def test_type_get_all(self):
        data = self.under_test.get_all()
        self.assertEqual(len(data), TestGedadRepository.DATA_SIZE)
        for d in data:
            self.assertEqual(type(d), Gedad)

    def test_type_get_all_using_filters(self):
        data = self.under_test.get_all({
            'limit': 2,
            'sort': '-id',
        })
        self.assertEqual(len(data), 2)
        self.assertEqual(type(data[0]), Gedad)
        self.assertEqual(data[0], Gedad(id=99, description='Todas las edades'))
