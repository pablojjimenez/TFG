import sqlite3


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBManager(metaclass=Singleton):
    def __init__(self, url: str):
        self.__connection = sqlite3.connect(url)

    @property
    def connection(self):
        return self.__connection

    def __del__(self):
        self.__connection.close()
