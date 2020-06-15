import os
from flask import Flask
from flask import render_template, request
from imdb_db_data_management.ImdbDataManager import ImdbDataManager


app = Flask(__name__)

imdb_data = ImdbDataManager()

@app.route('/')
def homepage_API_Detail():
    return render_template('index.html')


@app.route('/all-movies')
def get_all_movies():
    return imdb_data.get_all_movies()

@app.route('/search')
def search_by_film_title():
    return imdb_data.search_by_movie_title(request.args.get("title"))


if __name__ == '__main__':
    app.run()
