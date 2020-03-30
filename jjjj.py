

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, insert
engine = create_engine('sqlite:///movies.db', echo = True)
meta = MetaData()
conn = engine.connect()
# 1, oscar, ceballos, oceballos, mypassword
User = Table(
   'tb_user', meta, 
   Column('id', Integer, primary_key = True, autoincrement= True), 
   Column('name', String), 
   Column('last_name', String), 
   Column('user', String), 
   Column('password', String), 
)

#1, The Joker, 18+, 2019, La historia del archienemigo de batman.
Movies = Table(
   'tb_movies', meta, 
   Column('id', Integer, primary_key = True, autoincrement= True), 
   Column('name', String), 
   Column('ages_available', String), 
   Column('year', Integer), 
   Column('sinopsis', String), 
)

StatusMovies = Table(
   'tb_status_movies', meta, 
   Column('id', Integer, primary_key = True, autoincrement= True), 
   Column('id_user', String), 
   Column('id_movies', String), 
   Column('status_of_movie', Integer), 
)

#1,1,5,1,01/01/2020
Ranking = Table(
   'tb_ranking', meta, 
   Column('id', Integer, primary_key = True,autoincrement= True), 
   Column('id_movie', String, ForeignKey('tb_movies.id')), 
   Column('id_usuario', String, ForeignKey('tb_user.id')), 
   Column('date', String), 
)

#1,1,2,01/01/2020
Favoritos = Table(
   'tb_favorites', meta, 
   Column('id', Integer, primary_key = True, autoincrement= True), 
   Column('id_movie', String, ForeignKey('tb_movies.id')), 
   Column('id_usuario', String, ForeignKey('tb_user.id')), 
   Column('watched', Integer), #true
   Column('date', String), 
)

meta.create_all(engine)

#agregar favoritos
#agregar peliculas
#agregar usuarios
#rankear


def agregar_favoritos():
        nuevo_favorito = Favoritos.insert().\
            values(id_movie = 1, id_usuario = 1, date = "20/20/2020", watched = True)
        conn.execute(nuevo_favorito)
if __name__ == '__main__':
    agregar_favoritos()