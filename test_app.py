import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import (setup_db,
                    Actors,
                    Movies)

from dotenv import load_dotenv
load_dotenv('.env')

executive_producer_token = os.environ.get('EXECUTIVE_PRODUCER_TOKEN')
casting_director_token = os.environ.get('CASTING_DIRECTOR_TOKEN')
casting_assistant_token = os.environ.get('CASTING_ASSISTANT_TOKEN')


class IMDBTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ.get('TEST_DATABASE_URL')
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass

    '''Test for successfull /actors GET endpoint, for retriveing all actors.'''

    # Executive Producer

    def test_retrive_actors_executive_producer(self):
        res = self.client().get('/actors', headers=executive_producer_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Casting Director

    def test_retrive_actors_casting_director(self):
        res = self.client().get('/actors', headers=casting_director_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Casting Assistant

    def test_retrive_actors_casting_assistant(self):
        res = self.client().get('/actors', headers=casting_assistant_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    '''Test for successfull /movies GET endpoint, for retriveing all movies.'''

    # Executive Producer

    def test_retrive_movies_executive_producer(self):
        res = self.client().get('/movies', headers=executive_producer_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Casting Director

    def test_retrive_movies_casting_director(self):
        res = self.client().get('/movies', headers=casting_director_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Casting Assistant

    def test_retrive_movies_casting_assistant(self):
        res = self.client().get('/movies', headers=casting_assistant_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ''' For Unauthorized token or invalid token
     test for /movies and /actors GET endpoint '''

    '''Test for unsuccessfull /actors GET
    endpoint, for retriveing all actors.'''

    # Executive Producer

    def test_retrive_actors_executive_producer_unsuccessfull(self):
        res = self.client().get('/actors',
                                headers=os.environ.get('INVALID_TOKEN'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Casting Director

    def test_retrive_actors_casting_director_unsuccessfull(self):
        res = self.client().get('/actors',
                                headers=os.environ.get('INVALID_TOKEN'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Casting Assistant

    def test_retrive_actors_casting_assistant_unsuccessfull(self):
        res = self.client().get('/actors',
                                headers=os.environ.get('INVALID_TOKEN'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    '''Test for successfull /movies GET endpoint, for retriveing all movies.'''

    # Executive Producer

    def test_retrive_movies_executive_producer_unsuccessfull(self):
        res = self.client().get('/movies',
                                headers=os.environ.get('INVALID_TOKEN'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Casting Director

    def test_retrive_movies_casting_director_unsuccessfull(self):
        res = self.client().get('/movies',
                                headers=os.environ.get('INVALID_TOKEN'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Casting Assistant

    def test_retrive_movies_casting_assistant_unsuccessfull(self):
        res = self.client().get('/movies',
                                headers=os.environ.get('INVALID_TOKEN'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    ''' Test for deleting actors and movies form database'''

    def test_delete_actors_executive_producer(self):
        res = self.client().delete('/actors/6',
                                   headers=executive_producer_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_delete_actors_casting_director(self):
        res = self.client().delete('/actors/7',
                                   headers=casting_director_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_delete_actors_casting_assistant(self):
        res = self.client().delete('/actors/8',
                                   headers=casting_assistant_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    '''delete movies from database'''

    def test_delete_movies_executive_producer(self):
        res = self.client().delete('/movies/1',
                                   headers=executive_producer_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_delete_movies_casting_director(self):
        res = self.client().delete('/movies/7',
                                   headers=casting_director_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movies_casting_assistant(self):
        res = self.client().delete('/movies/8',
                                   headers=casting_assistant_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    ''' Delete non existing actors from database'''

    def test_delete_actors_executive_producer_not_found(self):
        res = self.client().delete('/actors/1000000000',
                                   headers=executive_producer_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    def test_delete_actors_casting_director_not_found(self):
        res = self.client().delete('/actors/100000000000',
                                   headers=casting_director_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    ''' Delete non existing movies from database'''

    def test_delete_movies_executive_producer_not_found(self):
        res = self.client().delete('/movies/10000000000',
                                   headers=executive_producer_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    ''' Post new actor to database'''

    def test_add_new_actor_executive_producer(self):
        actor_data = {
            'name': 'test name',
            'age': '50',
            'gender': 'female',
            'movie': 'test movie name'
        }

        res = self.client().post('/actors',
                                 headers=executive_producer_token,
                                 json=actor_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_add_new_actor_casting_director(self):
        actor_data = {
            'name': 'test name',
            'age': '50',
            'gender': 'female',
            'movie': 'test movie name'
        }

        res = self.client().post('/actors',
                                 headers=casting_director_token,
                                 json=actor_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_add_new_actor_casting_assistant(self):
        actor_data = {
            'name': 'test name',
            'age': '50',
            'gender': 'female',
            'movie': 'test movie name'
        }

        res = self.client().post('/actors',
                                 headers=casting_assistant_token,
                                 json=actor_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    '''Post new movie to database'''

    def test_add_new_movie_executive_producer(self):
        movie_data = {
            'title': 'test name',
            'rating': '50',
            'release_date': '2020-05-05',
            'actor': 'test movie name'
        }

        res = self.client().post('/movies',
                                 headers=executive_producer_token,
                                 json=movie_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_add_new_movie_casting_director(self):
        movie_data = {
            'title': 'test name',
            'rating': '50',
            'release_date': '2020-05-05',
            'actor': 'test movie name'
        }

        res = self.client().post('/movies',
                                 headers=casting_director_token,
                                 json=movie_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_add_new_movie_casting_assistant(self):
        movie_data = {
            'title': 'test name',
            'rating': '50',
            'release_date': '2020-05-05',
            'actor': 'test movie name'
        }

        res = self.client().post('/movies',
                                 headers=casting_assistant_token,
                                 json=movie_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    ''' update existing actor to database'''

    def test_add_update_actor_executive_producer(self):
        actor_data = {
            'name': 'test name',
            'age': '50',
            'gender': 'female',
            'movie': 'test movie name'
        }

        res = self.client().patch('/actors/10',
                                  headers=executive_producer_token,
                                  json=actor_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_add_update_actor_casting_director(self):
        actor_data = {
            'name': 'test name',
            'age': '50',
            'gender': 'female',
            'movie': 'test movie name'
        }

        res = self.client().patch('/actors/11',
                                  headers=casting_director_token,
                                  json=actor_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_add_update_actor_casting_assistant(self):
        actor_data = {
            'name': 'test name',
            'age': '50',
            'gender': 'female',
            'movie': 'test movie name'
        }

        res = self.client().patch('/actors/12',
                                  headers=casting_assistant_token,
                                  json=actor_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    '''patch update movie to database'''

    def test_add_update_movie_executive_producer(self):
        movie_data = {
            'title': 'test name',
            'rating': '50',
            'release_date': '2020-05-05',
            'actor': 'test movie name'
        }

        res = self.client().patch('/movies/10',
                                  headers=executive_producer_token,
                                  json=movie_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_add_update_movie_casting_director(self):
        movie_data = {
            'title': 'test name',
            'rating': '50',
            'release_date': '2020-05-05',
            'actor': 'test movie name'
        }

        res = self.client().patch('/movies/11',
                                  headers=casting_director_token,
                                  json=movie_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_add_update_movie_casting_assistant(self):
        movie_data = {
            'title': 'test name',
            'rating': '50',
            'release_date': '2020-05-05',
            'actor': 'test movie name'
        }

        res = self.client().patch('/movies/12',
                                  headers=casting_assistant_token,
                                  json=movie_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])


# Running the test
if __name__ == "__main__":
    unittest.main()
