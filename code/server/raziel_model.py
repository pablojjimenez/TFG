from abc import ABC, abstractmethod
from typing import Dict, Iterable


class MyModel(ABC):
    """
    Base father model for my problem to help some operations.
     - it adds dynamic attrs from a json
     - add `_dir()` method to get attr class representation
    """
    def __init__(self, data: Dict):
        if data: self._fill_attrs(data)

    def _dir(self) -> Iterable[str]:
        return list(filter(lambda x: x[:1] != '_' and '_' not in x, self.__dir__()))

    def _fill_attrs(self, data: Dict):
        for i in data.keys():
            setattr(self, i, data.get(i))

    @abstractmethod
    def _fill(self, data: Dict):
        pass

    def __str__(self) -> str:
        return str(vars(self))

    def get_tuple(self):
        return [str(getattr(self, i)) for i in self._dir()]


class Raziel(MyModel):
    N_MANDATORY_ATTRS = 15

    def __init__(self, data: Dict):
        if len(data) < 15:
            raise ValueError('Number of attrs incorrect to build a Raziel instance')
        super().__init__(data)

    def _fill(self, data: Dict):
        super()._fill_attrs(data)