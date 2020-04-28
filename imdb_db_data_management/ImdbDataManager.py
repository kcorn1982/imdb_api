from imdb_db_data_management.json_management.imdb_json_encoder import ImdbJsonEncoding
from imdb_db_data_management.sql_management.queries.imdb_query_manager import ImdbQueryManager

class ImdbDataManager:

    def __init__(self):
        self.json_encoder = ImdbJsonEncoding()
        self.imdb_query_manager = ImdbQueryManager()

    def get_all_movies(self):
        return self.json_encoder.encode_imdb_json(self.imdb_query_manager.get_all_movie_data())

    def search_by_movie_title(self, string_in_movie_title):
        return self.json_encoder.encode_imdb_json(self.imdb_query_manager.search_film_by_name(string_in_movie_title))

if __name__ == '__main__':
    x = ImdbDataManager()

