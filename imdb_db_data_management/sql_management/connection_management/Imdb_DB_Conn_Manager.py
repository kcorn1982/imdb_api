from psycopg2 import connect


class ImdbDBConnManager:

    def __init__(self, db='imdb', user='postgres', password='postgres', host='localhost', port=5432):
        self.connection = connect(dbname=db, user=user, password=password, host=host, port=port)
        self.cur = self.connection.cursor()

    def execute_query(self, query_string):
        return self.cur.execute(query_string)

    def return_data(self):
        return self.cur.fetchall()

    def close_connection(self):
        self.cur.close()


if __name__ == '__main__':
    x = ImdbDBConnManager()
    x.execute_query('SELECT * FROM moviedata')
    print(x.return_data())