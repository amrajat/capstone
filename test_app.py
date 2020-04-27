import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies

executive_producer_token = { 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTY5NzQ4LCJleHAiOjE1ODgwNTYxNDgsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ClIwbDlxrYsisRdL4nVKLDawrZRY75yNoiB7bIl31ubc8UvNmoVKo4uTpb7aSuUMd_WSD3qI5pKqICrjewpFYKsotih00GJCkjwn7uQLKiaXE6m-ur1jTMu3-HdsAPIKmjYQO40pIddr3ne4YtFpXtVdohoe1Kc9erBLMzYKldsTPihrVRGrHf0s4EdfKzS6dOCez5wU9Jm8e4Bs-9D33AAEFmjpADuLZN3sGA88EAA8TdxMPN7Wg34kcmkrw3xxTYzdEGpnhq5W6zGs9sq4ZQVMQGkcve1N1sg2s_QvVI1IUAGtnVbF1owW_ErRI8sxZncyZJI-fETjjztxIceVEA' }
casting_director_token = { 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTE4ZmQ3NGE5ODBhMGM4Njc5YTJhZCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTY5ODgzLCJleHAiOjE1ODgwNTYyODMsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.H9Taq4yTAzpLFiW1rgA-788LKyIe1DRx_bSoLSX_d69lPXXe5EZSAwp7H9gy87ta0bn9BYc_cXg_F00b7FLV0IO1wRtDhgipgY6k_EKz8x3sZ-ZzF2c5K2cZeA4UOp1Rp0kJ7RV2qixIBwaGgP4GQpGeTWW-VyOO92Gkc3qRlHQ1AVk6L-h2LleyqWYmUefOnXoaBK8PT6ylM6wkyMCnynZNAZbm3q5asG2pbx7AsrLMLb6XxQ1DGhJiEq-EHoeq3PEvDQotGUzrp-nU1rh_lngW9xmDRayDF3uWYoHMQj_rmOFKTD_T3xwtF70rxDArr41ygnneYMi09-6vNs7PSA' }
casting_assistant_token = { 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTViOTIzMWNjMWFjMGMxNDY3ZGE3YiIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTcwMDMwLCJleHAiOjE1ODgwNTY0MzAsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.G9TrHOWtiVTtmcvv86lYx31_hCthxvjdC50G8TJ1B4zh9FN_KtuQrJk5ckSewqJiV1ZYB4BjpP3vIZaET8EqvNiY0W7nXsg176qGJ5fY5BCa4dAWIV1wDoa8HMEBmzSIOBLKf1o4d9NfO0RuIu_0ZN7Xl_2JYXTPR7OPIKXYns4-ozE0M4Fqh3FHy6Mq8oMsd9Y8o3UFMUIMJOm6cHI65jsCihrPwXeCsGBjq0ldKH-xMAQIT2DMh4NilZmvxIJn8q17iBQBYmnpF_WW-M855NUPruwZBwlfIOKPBfF6OBH5RFTtNiwZ0Fec4-i5Z_PqwEx2EkecH7-3xtAz3tbg4Q' }

class IMDBTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', '12345', 'localhost:5432', 'capstone')
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


    ''' For Unauthorized token or invalid token test for /movies and /actors GET endpoint '''


    '''Test for unsuccessfull /actors GET endpoint, for retriveing all actors.'''

    # Executive Producer

    def test_retrive_actors_executive_producer_unsuccessfull(self):
        res = self.client().get('/actors', headers={"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTE5OTA0LCJleHAiOjE1ODc5MjcxMDQsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.HkP1AwAh1KDy1Cc9ZMflETXocgz4zDDxRO1Ea39go5y63i-6G_weVbEgZWK-FFRyxwYJTQdZ7v5yMMfjFm90jIDqqEnSs8Sxvligq9aHKseQIoBGVzzVTK-gfDHTSDOFadhgFsgOrPSkSmnWmvxmJ_zPmZZsyDeEMsgW1AhX8OuqUaUoYpKQvHLJOxyw2BaYY8dkRJSiGPQ293dpcefiZPib_1xdhCjdt8pWEWVgABrmUSx08ZGFnVn8Oa_y7Wsz4d4S2MBMrGSnw3FD1hv6WA8Sd3gXztZMGWm9vWt68dfjy4pkntHU1W1loesjUj1qM6fOKQKdAa2ndMOgmGTlGA"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Casting Director

    def test_retrive_actors_casting_director_unsuccessfull(self):
        res = self.client().get('/actors', headers={"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTE5OTA0LCJleHAiOjE1ODc5MjcxMDQsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.HkP1AwAh1KDy1Cc9ZMflETXocgz4zDDxRO1Ea39go5y63i-6G_weVbEgZWK-FFRyxwYJTQdZ7v5yMMfjFm90jIDqqEnSs8Sxvligq9aHKseQIoBGVzzVTK-gfDHTSDOFadhgFsgOrPSkSmnWmvxmJ_zPmZZsyDeEMsgW1AhX8OuqUaUoYpKQvHLJOxyw2BaYY8dkRJSiGPQ293dpcefiZPib_1xdhCjdt8pWEWVgABrmUSx08ZGFnVn8Oa_y7Wsz4d4S2MBMrGSnw3FD1hv6WA8Sd3gXztZMGWm9vWt68dfjy4pkntHU1W1loesjUj1qM6fOKQKdAa2ndMOgmGTlGA"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Casting Assistant

    def test_retrive_actors_casting_assistant_unsuccessfull(self):
        res = self.client().get('/actors', headers={"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTE5OTA0LCJleHAiOjE1ODc5MjcxMDQsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.HkP1AwAh1KDy1Cc9ZMflETXocgz4zDDxRO1Ea39go5y63i-6G_weVbEgZWK-FFRyxwYJTQdZ7v5yMMfjFm90jIDqqEnSs8Sxvligq9aHKseQIoBGVzzVTK-gfDHTSDOFadhgFsgOrPSkSmnWmvxmJ_zPmZZsyDeEMsgW1AhX8OuqUaUoYpKQvHLJOxyw2BaYY8dkRJSiGPQ293dpcefiZPib_1xdhCjdt8pWEWVgABrmUSx08ZGFnVn8Oa_y7Wsz4d4S2MBMrGSnw3FD1hv6WA8Sd3gXztZMGWm9vWt68dfjy4pkntHU1W1loesjUj1qM6fOKQKdAa2ndMOgmGTlGA"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    '''Test for successfull /movies GET endpoint, for retriveing all movies.'''

    # Executive Producer

    def test_retrive_movies_executive_producer_unsuccessfull(self):
        res = self.client().get('/movies', headers={"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTE5OTA0LCJleHAiOjE1ODc5MjcxMDQsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.HkP1AwAh1KDy1Cc9ZMflETXocgz4zDDxRO1Ea39go5y63i-6G_weVbEgZWK-FFRyxwYJTQdZ7v5yMMfjFm90jIDqqEnSs8Sxvligq9aHKseQIoBGVzzVTK-gfDHTSDOFadhgFsgOrPSkSmnWmvxmJ_zPmZZsyDeEMsgW1AhX8OuqUaUoYpKQvHLJOxyw2BaYY8dkRJSiGPQ293dpcefiZPib_1xdhCjdt8pWEWVgABrmUSx08ZGFnVn8Oa_y7Wsz4d4S2MBMrGSnw3FD1hv6WA8Sd3gXztZMGWm9vWt68dfjy4pkntHU1W1loesjUj1qM6fOKQKdAa2ndMOgmGTlGA"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Casting Director

    def test_retrive_movies_casting_director_unsuccessfull(self):
        res = self.client().get('/movies', headers={"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTE5OTA0LCJleHAiOjE1ODc5MjcxMDQsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.HkP1AwAh1KDy1Cc9ZMflETXocgz4zDDxRO1Ea39go5y63i-6G_weVbEgZWK-FFRyxwYJTQdZ7v5yMMfjFm90jIDqqEnSs8Sxvligq9aHKseQIoBGVzzVTK-gfDHTSDOFadhgFsgOrPSkSmnWmvxmJ_zPmZZsyDeEMsgW1AhX8OuqUaUoYpKQvHLJOxyw2BaYY8dkRJSiGPQ293dpcefiZPib_1xdhCjdt8pWEWVgABrmUSx08ZGFnVn8Oa_y7Wsz4d4S2MBMrGSnw3FD1hv6WA8Sd3gXztZMGWm9vWt68dfjy4pkntHU1W1loesjUj1qM6fOKQKdAa2ndMOgmGTlGA"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    # Casting Assistant

    def test_retrive_movies_casting_assistant_unsuccessfull(self):
        res = self.client().get('/movies', headers={"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTE5OTA0LCJleHAiOjE1ODc5MjcxMDQsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.HkP1AwAh1KDy1Cc9ZMflETXocgz4zDDxRO1Ea39go5y63i-6G_weVbEgZWK-FFRyxwYJTQdZ7v5yMMfjFm90jIDqqEnSs8Sxvligq9aHKseQIoBGVzzVTK-gfDHTSDOFadhgFsgOrPSkSmnWmvxmJ_zPmZZsyDeEMsgW1AhX8OuqUaUoYpKQvHLJOxyw2BaYY8dkRJSiGPQ293dpcefiZPib_1xdhCjdt8pWEWVgABrmUSx08ZGFnVn8Oa_y7Wsz4d4S2MBMrGSnw3FD1hv6WA8Sd3gXztZMGWm9vWt68dfjy4pkntHU1W1loesjUj1qM6fOKQKdAa2ndMOgmGTlGA"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    ''' Test for deleting actors and movies form database'''

    def test_delete_actors_executive_producer(self):
        res = self.client().delete('/actors/6', headers=executive_producer_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_delete_actors_casting_director(self):
        res = self.client().delete('/actors/7', headers=casting_director_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_delete_actors_casting_assistant(self):
        res = self.client().delete('/actors/8', headers=casting_assistant_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    '''delete movies from database'''

    def test_delete_movies_executive_producer(self):
        res = self.client().delete('/movies/1', headers=executive_producer_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_delete_movies_casting_director(self):
        res = self.client().delete('/movies/7', headers=casting_director_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movies_casting_assistant(self):
        res = self.client().delete('/movies/8', headers=casting_assistant_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    ''' Delete non existing actors from database'''
    def test_delete_actors_executive_producer_not_found(self):
        res = self.client().delete('/actors/1000000000', headers=executive_producer_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    def test_delete_actors_casting_director_not_found(self):
        res = self.client().delete('/actors/100000000000', headers=casting_director_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    ''' Delete non existing movies from database'''
    def test_delete_movies_executive_producer_not_found(self):
        res = self.client().delete('/movies/10000000000', headers=executive_producer_token)
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

        res = self.client().post('/actors', headers=executive_producer_token, json=actor_data)
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

        res = self.client().post('/actors', headers=casting_director_token, json=actor_data)
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

        res = self.client().post('/actors', headers=casting_assistant_token, json=actor_data)
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

        res = self.client().post('/movies', headers=executive_producer_token, json=movie_data)
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

        res = self.client().post('/movies', headers=casting_director_token, json=movie_data)
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

        res = self.client().post('/movies', headers=casting_assistant_token, json=movie_data)
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

        res = self.client().patch('/actors/10', headers=executive_producer_token, json=actor_data)
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

        res = self.client().patch('/actors/11', headers=casting_director_token, json=actor_data)
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

        res = self.client().patch('/actors/12', headers=casting_assistant_token, json=actor_data)
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

        res = self.client().patch('/movies/10', headers=executive_producer_token, json=movie_data)
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

        res = self.client().patch('/movies/11', headers=casting_director_token, json=movie_data)
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

        res = self.client().patch('/movies/12', headers=casting_assistant_token, json=movie_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

# Running the test
if __name__ == "__main__":
    unittest.main()
