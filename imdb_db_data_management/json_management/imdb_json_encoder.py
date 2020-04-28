import json

from flask import jsonify


class ImdbJsonEncoding:

    def __init__(self):
        self.field_names = ['movie_id', 'movie_title','duration', 'color', 'director_name', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'gross', 'genres', 'plot_keywords', 'language', 'country', 'content_rating', 'budget', 'title_year', 'imdb_score']

    def _create_imdb_dict_array(self, array_of_results):
        array_of_results_dict = []

        if len(array_of_results) == 1:
            array_of_results_dict.append(dict(zip(self.field_names, array_of_results)))
            return array_of_results_dict
        elif len(array_of_results) > 1:
            for result in array_of_results:
                array_of_results_dict.append(dict(zip(self.field_names, result)))
            return array_of_results_dict
        else:
            return "No Movies found"

    def encode_imdb_json(self, results):
        return jsonify(self._create_imdb_dict_array(results))

