from abc import *

class DBController:
    db = None
    cursor = None

    @abstractmethod
    def connect(self, dbname='testdb', host='localhost', user='tails1101', password='000000', port=5432):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def executeQuery(self, query):
        pass