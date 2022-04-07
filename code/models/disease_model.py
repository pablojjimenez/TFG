from models.exceptions import NoCorrectTypeException
from models.small_models import Cie


class Disease:
    def __init__(self, id, name, cie):
        self.id = id
        self.name = name
        self._validate_cie(cie)

    @property
    def cie(self):
        return self._cie

    def _validate_cie(self, value):
        if not isinstance(value, Cie) and value is not None:
            raise NoCorrectTypeException('Must be Cie object or None')
        self._cie = value
