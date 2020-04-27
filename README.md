# Casting Agency
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

##Motivation
I found this project very interesting.
## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

##### ENVIRONMENTAL  VARIABLES
```bash
export DATABASE_URL=your database url
export SECRET_KEY = you app secret key
```

## Running the server

First ensure you are working using your created virtual environment.

To run the server, execute:
Note: If you're on windows os replace `export` to `set`
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

## Testing
To run the tests, run
```

python test_app.py
```

## Database Migration
for database migration, run
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## API Reference

### Getting Started:
- Base URL: At this time this app can only run on local server at `http://127.0.0.1:5000/`, which is set as proxy in the frontend configuration.

- Authentication: This app does not require authentication or API keys.
### Authentication:
authentication is required to communicate with api.
### Error Handling
Errors are returned as json objects in the following format:
```
{
    'success': True,
    'error': 404,
    'message': 'not found'
}
```
The API will return three error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable

## Endpoints

### GET/actors

```
curl --location --request GET 'https://udacity-capstone-project.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTY5NzQ4LCJleHAiOjE1ODgwNTYxNDgsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ClIwbDlxrYsisRdL4nVKLDawrZRY75yNoiB7bIl31ubc8UvNmoVKo4uTpb7aSuUMd_WSD3qI5pKqICrjewpFYKsotih00GJCkjwn7uQLKiaXE6m-ur1jTMu3-HdsAPIKmjYQO40pIddr3ne4YtFpXtVdohoe1Kc9erBLMzYKldsTPihrVRGrHf0s4EdfKzS6dOCez5wU9Jm8e4Bs-9D33AAEFmjpADuLZN3sGA88EAA8TdxMPN7Wg34kcmkrw3xxTYzdEGpnhq5W6zGs9sq4ZQVMQGkcve1N1sg2s_QvVI1IUAGtnVbF1owW_ErRI8sxZncyZJI-fETjjztxIceVEA'
```

Response
```
{
  "actors": [
    {
      "age": 40,
      "gender": "male",
      "id": 1,
      "movie": "matrix",
      "name": "actor name"
    }
  ],
  "success": true,
  "total_actors": 1
}
```

### GET/movies

```
curl --location --request GET 'https://udacity-capstone-project.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTY5NzQ4LCJleHAiOjE1ODgwNTYxNDgsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ClIwbDlxrYsisRdL4nVKLDawrZRY75yNoiB7bIl31ubc8UvNmoVKo4uTpb7aSuUMd_WSD3qI5pKqICrjewpFYKsotih00GJCkjwn7uQLKiaXE6m-ur1jTMu3-HdsAPIKmjYQO40pIddr3ne4YtFpXtVdohoe1Kc9erBLMzYKldsTPihrVRGrHf0s4EdfKzS6dOCez5wU9Jm8e4Bs-9D33AAEFmjpADuLZN3sGA88EAA8TdxMPN7Wg34kcmkrw3xxTYzdEGpnhq5W6zGs9sq4ZQVMQGkcve1N1sg2s_QvVI1IUAGtnVbF1owW_ErRI8sxZncyZJI-fETjjztxIceVEA'
```

Response
```
{
  "movies": [
    {
      "actor": "patched actor",
      "id": 1,
      "rating": 40,
      "release_date": "Tue, 02 Feb 2010 00:00:00 GMT",
      "title": "patched new added"
    }
  ],
  "success": true,
  "total_movies": 1
}
```

### DELETE/movies/1
```
curl --location --request DELETE 'https://udacity-capstone-project.herokuapp.com/movies/1' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTY5NzQ4LCJleHAiOjE1ODgwNTYxNDgsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ClIwbDlxrYsisRdL4nVKLDawrZRY75yNoiB7bIl31ubc8UvNmoVKo4uTpb7aSuUMd_WSD3qI5pKqICrjewpFYKsotih00GJCkjwn7uQLKiaXE6m-ur1jTMu3-HdsAPIKmjYQO40pIddr3ne4YtFpXtVdohoe1Kc9erBLMzYKldsTPihrVRGrHf0s4EdfKzS6dOCez5wU9Jm8e4Bs-9D33AAEFmjpADuLZN3sGA88EAA8TdxMPN7Wg34kcmkrw3xxTYzdEGpnhq5W6zGs9sq4ZQVMQGkcve1N1sg2s_QvVI1IUAGtnVbF1owW_ErRI8sxZncyZJI-fETjjztxIceVEA'
```
Response
```
{
  "delete": 1,
  "success": true
}
```



### DELETE/actors/1

```
curl --location --request DELETE 'https://udacity-capstone-project.herokuapp.com/actors/1' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTY5NzQ4LCJleHAiOjE1ODgwNTYxNDgsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ClIwbDlxrYsisRdL4nVKLDawrZRY75yNoiB7bIl31ubc8UvNmoVKo4uTpb7aSuUMd_WSD3qI5pKqICrjewpFYKsotih00GJCkjwn7uQLKiaXE6m-ur1jTMu3-HdsAPIKmjYQO40pIddr3ne4YtFpXtVdohoe1Kc9erBLMzYKldsTPihrVRGrHf0s4EdfKzS6dOCez5wU9Jm8e4Bs-9D33AAEFmjpADuLZN3sGA88EAA8TdxMPN7Wg34kcmkrw3xxTYzdEGpnhq5W6zGs9sq4ZQVMQGkcve1N1sg2s_QvVI1IUAGtnVbF1owW_ErRI8sxZncyZJI-fETjjztxIceVEA'
```

Response

```
{
  "delete": 1,
  "success": true
}
```

### POST/actors
```
curl --location --request POST 'https://udacity-capstone-project.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTY5NzQ4LCJleHAiOjE1ODgwNTYxNDgsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ClIwbDlxrYsisRdL4nVKLDawrZRY75yNoiB7bIl31ubc8UvNmoVKo4uTpb7aSuUMd_WSD3qI5pKqICrjewpFYKsotih00GJCkjwn7uQLKiaXE6m-ur1jTMu3-HdsAPIKmjYQO40pIddr3ne4YtFpXtVdohoe1Kc9erBLMzYKldsTPihrVRGrHf0s4EdfKzS6dOCez5wU9Jm8e4Bs-9D33AAEFmjpADuLZN3sGA88EAA8TdxMPN7Wg34kcmkrw3xxTYzdEGpnhq5W6zGs9sq4ZQVMQGkcve1N1sg2s_QvVI1IUAGtnVbF1owW_ErRI8sxZncyZJI-fETjjztxIceVEA' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "patched new added", "age": "40", "gender":"f", "movie":"patched movie"}'
```
Response
```
{
  "actors": {
    "age": 40,
    "gender": "f",
    "id": 2,
    "movie": "patched movie",
    "name": "patched new added"
  },
  "success": true
}
```


### POST/movies
```
curl --location --request POST 'https://udacity-capstone-project.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTY5NzQ4LCJleHAiOjE1ODgwNTYxNDgsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ClIwbDlxrYsisRdL4nVKLDawrZRY75yNoiB7bIl31ubc8UvNmoVKo4uTpb7aSuUMd_WSD3qI5pKqICrjewpFYKsotih00GJCkjwn7uQLKiaXE6m-ur1jTMu3-HdsAPIKmjYQO40pIddr3ne4YtFpXtVdohoe1Kc9erBLMzYKldsTPihrVRGrHf0s4EdfKzS6dOCez5wU9Jm8e4Bs-9D33AAEFmjpADuLZN3sGA88EAA8TdxMPN7Wg34kcmkrw3xxTYzdEGpnhq5W6zGs9sq4ZQVMQGkcve1N1sg2s_QvVI1IUAGtnVbF1owW_ErRI8sxZncyZJI-fETjjztxIceVEA' \
--header 'Content-Type: application/json' \
--data-raw '{"title": "patched new added", "rating": "40", "release_date":"2010-02-02", "actor":"patched actor"}'
```
Response
```
{
  "movies": {
    "actor": "patched actor",
    "id": 2,
    "rating": 40,
    "release_date": "Tue, 02 Feb 2010 00:00:00 GMT",
    "title": "patched new added"
  },
  "success": true
}
```


### PATCH/actors/id
```
curl --location --request PATCH 'https://udacity-capstone-project.herokuapp.com/actors/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTY5NzQ4LCJleHAiOjE1ODgwNTYxNDgsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ClIwbDlxrYsisRdL4nVKLDawrZRY75yNoiB7bIl31ubc8UvNmoVKo4uTpb7aSuUMd_WSD3qI5pKqICrjewpFYKsotih00GJCkjwn7uQLKiaXE6m-ur1jTMu3-HdsAPIKmjYQO40pIddr3ne4YtFpXtVdohoe1Kc9erBLMzYKldsTPihrVRGrHf0s4EdfKzS6dOCez5wU9Jm8e4Bs-9D33AAEFmjpADuLZN3sGA88EAA8TdxMPN7Wg34kcmkrw3xxTYzdEGpnhq5W6zGs9sq4ZQVMQGkcve1N1sg2s_QvVI1IUAGtnVbF1owW_ErRI8sxZncyZJI-fETjjztxIceVEA' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "patched new added", "age": "40", "gender":"f", "movie":"patched movie"}'
```

Response
```
{
  "actor": [
    {
      "age": 40,
      "gender": "f",
      "id": 2,
      "movie": "patched movie",
      "name": "patched new added"
    }
  ],
  "success": true
}
```



### PATCH/movies/id
```
curl --location --request PATCH 'https://udacity-capstone-project.herokuapp.com/movies/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxtMmNKcDRWeTEwbzRZTVhaUS14TyJ9.eyJpc3MiOiJodHRwczovL3dlYi1zZWN1cmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTFhMGZmZmVjNGQwMGUxZDViOTk3MCIsImF1ZCI6IklNREIgQVBJIiwiaWF0IjoxNTg3OTY5NzQ4LCJleHAiOjE1ODgwNTYxNDgsImF6cCI6Ik1wWlV2R1c1T1RIZHI1d2ZzRWlHNkxWN2ZOMXFsMjR1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ClIwbDlxrYsisRdL4nVKLDawrZRY75yNoiB7bIl31ubc8UvNmoVKo4uTpb7aSuUMd_WSD3qI5pKqICrjewpFYKsotih00GJCkjwn7uQLKiaXE6m-ur1jTMu3-HdsAPIKmjYQO40pIddr3ne4YtFpXtVdohoe1Kc9erBLMzYKldsTPihrVRGrHf0s4EdfKzS6dOCez5wU9Jm8e4Bs-9D33AAEFmjpADuLZN3sGA88EAA8TdxMPN7Wg34kcmkrw3xxTYzdEGpnhq5W6zGs9sq4ZQVMQGkcve1N1sg2s_QvVI1IUAGtnVbF1owW_ErRI8sxZncyZJI-fETjjztxIceVEA' \
--header 'Content-Type: application/json' \
--data-raw '{"title": "new added", "rating": "40", "release_date":"2020-02-02", "actor":"new"}'
```

Response
```
{
  "movie": [
    {
      "actor": "new",
      "id": 2,
      "rating": 40,
      "release_date": "Sun, 02 Feb 2020 00:00:00 GMT",
      "title": "new added"
    }
  ],
  "success": true
}
```


### Roles
there are 3 different types of token or permissions so they can perform action accordingly.

- Casting Assistant
    - Can view actors and movies
- Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies
- Executive Producer
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database

## Deployment to Heroku
clone this repo to you github account connect this repo to you heroku account. and set environmental varials in heroku config vars section.

## Authors
Yours truly, R

## Acknowledgements 
The awesome team at Udacity and all of the students.