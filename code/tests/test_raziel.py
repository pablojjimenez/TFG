import unittest

from models.disease_model import Disease
from models.exceptions import InvalidIDException, NoAttributeException, \
    NoCorrectTypeException
from models.raziel_model import Raziel
from models.small_models import Cie, Sex, Ccaa, Gedad


class TestRaziel(unittest.TestCase):
    JSON_DATA = {}

    def setUp(self):
        TestRaziel.JSON_DATA = {
            'id': None,
            'ano': 2020,
            'causa': Disease(2, 'reason', Cie(1, '')),
            'sexo': Sex.FEMALE,
            'ccaas': Ccaa(1, ''),
            'gedad': Gedad(1, ''),
            'defu': 0,
            'avp': 0,
            'cruda': 0.0,
            'tavp': 0.0,
            'edad': 2.9,
            'tasae': 0.0,
            'tavpe': 0.0,
            'tasaw': 0.0,
            'tasavpw': 0.0
        }

    def test_should_create_Raziel_with_all_field_none(self):
        with self.assertRaises(NoAttributeException):
            Raziel({'attr_random': 23})

    def test_create_correct_raziel_object_from_json(self):
        TestRaziel.JSON_DATA['id'] = 2
        raziel = Raziel(TestRaziel.JSON_DATA)
        self.assertIsInstance(raziel, Raziel)

    def test_create_incorrect_raziel_object_from_json(self):
        with self.assertRaises(NoCorrectTypeException):
            TestRaziel.JSON_DATA['gedad'] = 2
            Raziel(TestRaziel.JSON_DATA)

    def test_create_correct_raziel_id_provided(self):
        TestRaziel.JSON_DATA['id'] = 1
        r = Raziel(TestRaziel.JSON_DATA)
        self.assertEqual(r.id, 1)

    def test_create_correct_raziel_id_not_provided(self):
        with self.assertRaises(InvalidIDException):
            Raziel(TestRaziel.JSON_DATA)

    def test_create_incorrect_raziel_id(self):
        with self.assertRaises(InvalidIDException):
            TestRaziel.JSON_DATA['id'] = -1
            Raziel(TestRaziel.JSON_DATA)
