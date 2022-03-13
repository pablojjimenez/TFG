from models.exceptions import NoCorrectTypeException
from models.small_models import Cie


class Disease:
    def __init__(self, id, name, cie):
        self.id = id
        self.name = name
        self.cie = cie

    @property
    def cie(self):
        return self._cie

    @cie.setter
    def cie(self, value):
        if not isinstance(value, Cie):
            raise NoCorrectTypeException('Must be Cie object')
        self._cie = value
