from flask import Flask, render_template, request, url_for, redirect
from functions import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_people_list', methods=['GET', 'POST'])
def get_people_list():
    people = get_people()
    return render_template('person_list.html', Person=people)


@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        born = request.form['born']
        name = request.form['name']
        if add_new_person(born, name) == False:
            return render_template("warning.html")
    return render_template('add_person.html')


@app.route('/delete_person', methods=['GET', 'POST'])
def delete_person():
    if request.method == 'POST':
        name = request.form['name']
        delete_one_person(name)
    people = get_people()
    return render_template('delete_person.html', people=people)


@app.route('/find_person', methods=['GET', 'POST'])
def find_person():
    if request.method == 'POST':
        name = request.form['name']
        searched_person = find_a_person(name)
        movies = get_actor_movies(name)
        if searched_person:
            return render_template('searched_person.html', searched_person=searched_person, movies=movies)
    people = get_people()
    return render_template('find_person.html', people=people)


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        tagline = request.form['tagline']
        title = request.form['title']
        released = request.form['released']
        if add_new_movie(tagline, title, released) == False:
            return render_template('warning.html')
    return render_template('add_movie.html')


@app.route('/get_movie_list', methods=['GET', 'POST'])
def get_movie_list():
    movies = get_movies()
    return render_template('list_movies.html', movies=movies)


@app.route('/delete_movie', methods=['GET', 'POST'])
def delete_movie():
    if request.method == 'POST':
        title = request.form['title']
        delete_one_movie(title)
    movies = get_movies()
    return render_template('delete_movie.html', movies=movies)


@app.route('/find_movie', methods=['GET', 'POST'])
def find_movie():
    if request.method == 'POST':
        title = request.form['title']
        searched_movie = find_a_movie(title)
        actors = get_actors(title)
        directors = get_directors(title)
        if searched_movie:
            return render_template('searched_movie.html', searched_movie=searched_movie, actors=actors,
                                   directors=directors)
    movies = get_movies()
    return render_template('find_movie.html', movies=movies)


@app.route('/add_actor_movie', methods=['GET', 'POST'])
def add_actor_movie():
    if request.method == 'POST':
        title = request.form['title']
        name = request.form['name']
        add_actor_to_movie(name, title)
    actors = get_people()
    movies = get_movies()
    return render_template('add_actor_movie.html', movies=movies, actors = actors)