from flask import Flask, render_template, redirect, request, url_for 
from random import choice
from flask_sqlalchemy import SQLAlchemy

web_site = Flask(__name__)

web_site.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(web_site)

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(db.Model):
  __tablename__ = 'tb_user'
  id = Column('id', Integer, primary_key = True, autoincrement= True)
  name = Column('name', String)
  last_name = Column('last_name', String)
  username = Column('username', String)
  password = Column('password', String)


class Movie(db.Model): 
  __tablename__='tb_movies'
  id= Column('id', Integer, primary_key = True, autoincrement= True) 
  name = Column('name', String) 
  ages_available = Column('ages_available', String) 
  year = Column('year', Integer) 
  sinopsis = Column('sinopsis', String) 


# class FavouriteMovie(db.Model):
#   __tablename__=  'tb_favorites'
#   id = Column('id', Integer, primary_key = True, autoincrement= True)
#   movie = relationship(Movie, back_populates="movies")
#   user = relationship(User, back_populates='user') 
#   watched = Column('watched', Integer) #true
#   date = Column('date', String)

db.create_all()

@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route('/movies/create_a_movie')
def add_movies():
  return render_template("agregar_pelicula.html")

@web_site.route('/movies/new', methods=['POST'])
def handle_data():
  if request.form:
    vname = request.form.get('name',"no name")
    vages_available = request.form['ages_available']
    vyear = request.form.get('year')
    if not vyear:
      return 500
    vsinopsis = request.form['sinopsis']
    newMovie = Movie(name= vname, ages_available= vages_available, year= vyear, sinopsis= vsinopsis)
    db.session.add(newMovie)
    db.session.commit()
  return render_template('success_add_movie.html')

@web_site.route('/user/create_a_use')
def add_user():
  return render_template("agregar_usuario.html")

@web_site.route('/user/new', methods=['POST'])
def handle_data_user():
  if request.form:
    vname = request.form.get('name',"no name")
    vlastname = request.form['last_name']
    vusername = request.form.get('username')
    if not vusername:
      return 500
    vpassword = request.form['password']
    newUser = User(name= vname, last_name= vlastname, username= vusername, password= vpassword)
    db.session.add(newUser)
    db.session.commit()
  return render_template('success_add_user.html')

@web_site.route('/user/list_name')
def add_user():
  return render_template("agregar_usuario.html")


web_site.run(host='0.0.0.0', port=8080)