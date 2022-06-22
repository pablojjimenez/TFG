from models.exceptions import NoCorrectTypeException
from models.small_models import Cie


class Disease:
    """
    Description:
        Disease is the abstraction of the data stored in the diseases CSV. This class provides some
        types and constraint validation
    Properties:
        id: int - identification
        name: str - disease name
        cie: Cie - Cie object representation that can be None
    """
    def __init__(self, id, name, cie):
        self.id = id
        self.name = name
        self._validate_cie(cie)

    def _validate_cie(self, value):
        if not isinstance(value, Cie) and value is not None:
            raise NoCorrectTypeException('Must be Cie object or None')
        self.cie = value
