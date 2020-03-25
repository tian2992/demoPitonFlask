from flask import Flask, render_template, redirect, request, url_for 
from random import choice
from flask_sqlalchemy import SQLAlchemy

web_site = Flask(__name__)

web_site.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(web_site)

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
  __tablename__ = 'tb_user'
  id = Column('id', Integer, primary_key = True, autoincrement= True)
  name = Column('name', String)
  last_name = Column('last_name', String)
  username = Column('username', String)
  password = Column('password', String)
  
  favs = relationship("FavoriteMovie", back_populates="user")

class Movie(db.Model): 
  __tablename__='tb_movies'
  id= Column('id', Integer, primary_key = True, autoincrement= True) 
  name = Column('name', String) 
  ages_available = Column('ages_available', String) 
  year = Column('year', Integer) 
  sinopsis = Column('sinopsis', String) 

  favs = relationship("FavoriteMovie", back_populates="movie")



class FavoriteMovie(db.Model):
  __tablename__=  'tb_favorites'
  id = Column('id', Integer, primary_key = True, autoincrement= True)
  user_id = Column(Integer, ForeignKey(User.id))
  movie_id = Column(Integer, ForeignKey(Movie.id))

  movie = relationship(Movie, back_populates="favs")
  user = relationship(User, back_populates='favs') 
  watched = Column('watched', Integer) #true
  date = Column('date', String)

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

@web_site.route('/user/create_a_user')
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
def list_users():
    listUser = User.query.order_by(User.id.desc()).all()
    return render_template("listado_usuarios.html", users = listUser, rows = len(listUser))   

# /user/<user>/new_favourite/<movie_id>

@web_site.route('/user/<int:user>/new_favourite/<int:movie_id>')
def crear_favorito(user, movie_id):
  v_visto = request.form['v_visto']
  v_fecha = reques.form['fecha']

  favorito = FavoriteMovie(user_id = user,movie_id = movie_id,watched = v_visto, date = v_fecha)
  db.session.add(favorito)
  db.session.commit()
  
  return render_template('<p>Registro agregado</p>')

@web_site.route('/movies/list')
def list_movies():
  lista = Movie.query.order_by(Movie.id.desc()).all()
  


web_site.run(host='0.0.0.0', port=8080)