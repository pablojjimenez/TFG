
class Disease:
    def __init__(self, name: str, cie: str):
        if not isinstance(name, str) and not isinstance(cie, str):
            raise ValueError('attrs must be str')
        self.name = name
        self.cie = cie

    def __str__(self) -> str:
        return str(vars(self))
