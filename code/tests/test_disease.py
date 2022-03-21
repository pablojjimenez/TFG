import unittest

from models.disease_model import Disease
from models.exceptions import NoCorrectTypeException
from models.small_models import Cie


class TestDisease(unittest.TestCase):

    def setUp(self):
        self.data = Disease(id='hola', name='hola', cie=Cie(1, ''))

    def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.data, str)

    def test_should_not_admit_change_cie(self):
        with self.assertRaises(NoCorrectTypeException):
            self.data.cie = 10
