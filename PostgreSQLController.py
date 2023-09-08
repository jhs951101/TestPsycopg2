import DBController;
import psycopg2

class PostgreSQLController(DBController.DBController):
    db = None
    cursor = None

    def connect(self, dbname='testdb', host='localhost', user='tails1101', password='000000', port=5432):
        try:
            self.db = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
            self.cursor = self.db.cursor()
        except:
            self.db = None

    def disconnect(self):
        try:
            if self.db is not None:
                self.db.close()
        except:
            print(end='')
        
        try:
            if self.cursor is not None:
                self.cursor.close()
        except:
            print(end='')

    def executeQuery(self, query):
        result = False

        try:
            if self.db is not None:
                if query is not None:
                    if len(query) >= 1:
                        query = query.strip()
                        self.cursor.execute(query)

                        if query[0:6] == 'SELECT':
                            result = self.cursor.fetchall()
                        else:
                            self.db.commit()
                            result = True
        except:
            print(end='')

        return result