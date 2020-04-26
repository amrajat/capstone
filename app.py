import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movies, Actors
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    app.secret_key = 'hard'  # os.environ.get('SECRET_KEY')

    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response

    # Get all the data of actors from database
    @app.route('/actors', methods=['GET'])
    @requires_auth(permission='get:actors')
    def get_all_actors(payload):
        try:
            if request.method == 'GET':
                selection = Actors.query.all()
                return jsonify({
                    'success': True,
                    'actors': [a.format() for a in selection],
                    'total_actors': len(selection)
                }), 200

            else:
                abort(405)
        except:
            abort(422)

    # Get all the data of movies from database
    @app.route('/movies', methods=['GET'])
    @requires_auth(permission='get:movies')
    def get_all_movies(payload):
        try:
            if request.method == 'GET':
                selection = Movies.query.all()
                return jsonify({
                    'success': True,
                    'movies': [m.format() for m in selection],
                    'total_movies': len(selection)
                }), 200

            else:
                abort(405)
        except:
            abort(422)

    # Delete actor by id from database
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth(permission='delete:actors')
    def delete_actor_by_id(payload, id):

        actor_to_be_deleted = Actors.query.get(id)

        if actor_to_be_deleted is None:
            abort(404)

        actor_to_be_deleted.delete()

        return jsonify({
            'success': True,
            'delete': id
        }), 200

    # Delete movie by id from database
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth(permission='delete:movies')
    def delete_movie_by_id(payload, id):

        movie_to_be_deleted = Movies.query.get(id)

        if movie_to_be_deleted is None:
            abort(404)

        movie_to_be_deleted.delete()

        return jsonify({
            'success': True,
            'delete': id
        }), 200

    # adds new actor to database
    @app.route('/actors', methods=['POST'])
    @requires_auth(permission='post:actors')
    def post_actor_details(payload):
        body = request.get_json()
        name = body['name']
        age = body['age']
        gender = body['gender']
        movie = body['movie']
        new_actor = Actors(name=name, age=age, gender=gender, movie=movie)
        new_actor.insert()
        new_actor_data = Actors.query.order_by(-Actors.id).first().format()
        return jsonify({
            'success': True,
            'actors': new_actor_data
        })

    # adds new movie to database
    @app.route('/movies', methods=['POST'])
    @requires_auth(permission='post:movies')
    def post_movie_details(payload):
        body = request.get_json()
        title = body['title']
        release_date = body['release_date']
        rating = body['rating']
        actor = body['actor']
        new_movie = Movies(
            title=title, release_date=release_date, actor=actor, rating=rating)
        new_movie.insert()
        new_movie_data = Movies.query.order_by(-Movies.id).first().format()
        return jsonify({
            'success': True,
            'movies': new_movie_data
        })
    # update the existing actor by id to database
    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth(permission='patch:actors')
    def update_existing_actor(payload, id):
        actor = Actors.query.filter(Actors.id == id).one_or_none()
        if not actor:
            abort(404)
        body = request.get_json()
        actor.name = body.get('name', actor.name)
        actor.age = body.get('age', actor.age)
        actor.gender = body.get('gender', actor.gender)
        actor.movie = body.get('movie', actor.movie)
        actor.update()
        return jsonify({
            'success': True,
            'actor': [actor.format()]
        })

    # update the existing movie by id to database
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth(permission='patch:movies')
    def update_existing_movie(payload, id):
        movie = Movies.query.filter(Movies.id == id).one_or_none()
        if not movie:
            abort(404)
        body = request.get_json()
        movie.title = body.get('title', movie.title)
        movie.release_date = body.get('release_date', movie.release_date)
        movie.rating = body.get('rating', movie.rating)
        movie.actor = body.get('actor', movie.actor)
        movie.update()
        return jsonify({
            'success': True,
            'movie': [movie.format()]
        })
        abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable'
        }), 422

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Authorization Error"
        }), 401

    return app
app = create_app()
if __name__ == "__main__":
    app.run(debug=False)