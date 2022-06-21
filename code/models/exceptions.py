class NoCorrectTypeException(Exception):
    def __init__(self, sms):
        Exception.__init__(self, sms)


class NoAttributeException(Exception):
    def __init__(self, sms):
        Exception.__init__(self, sms)


class InvalidIDException(Exception):
    def __init__(self, sms):
        Exception.__init__(self, sms)


class IncorrectColumnNamesException(Exception):
    def __init__(self, sms):
        Exception.__init__(self, sms)


class IncorrectQueryException(Exception):
    def __init__(self, sms):
        sms += ". example of use: '{'gedad': ('==', 99), 'causa': ('==', 999), 'ccaa': ('==', 99)}'"
        Exception.__init__(self, sms)


class DataIsNotAvaible(Exception):
    def __init__(self, file_name):
        Exception.__init__(self, f"Data files are not available, opening {file_name}")
