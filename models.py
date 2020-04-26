import os
from sqlalchemy import Column, String, Integer, Date, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

#database_name = "capstone"
#database_password = 12345#os.environ.get('DATABASE_PASSWORD')
database_path = os.environ['DATABASE_URL']
#database_path = "postgres://{}:{}@{}/{}".format('postgres', str(database_password), 'localhost:5432', database_name)
secret_key = os.environ['SECRET_KEY']
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    app.secret_key = secret_key
    db.init_app(app)
    #db.create_all()

'''
Movie Model

'''
class Movies(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = Column(Date)
  rating = Column(Integer)
  actor = Column(String)

  def __init__(self, title, release_date, rating, actor):
    self.title = title
    self.release_date = release_date
    self.rating = rating
    self.actor = actor

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date,
      'rating': self.rating,
      'actor': self.actor
    }

'''
Actor Model

'''
class Actors(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)
  movie = Column(String)

  def __init__(self, name, age, gender, movie):
    self.name = name
    self.age = age
    self.gender = gender
    self.movie = movie

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender,
      'movie': self.movie
    }