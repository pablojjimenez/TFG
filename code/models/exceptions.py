class NoCorrectTypeException(Exception):
    def __init__(self, sms):
        Exception.__init__(self, sms)


class NoAttributeException(Exception):
    def __init__(self, sms):
        Exception.__init__(self, sms)
