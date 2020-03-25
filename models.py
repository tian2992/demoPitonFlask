from sqlalchemy import Column, Integer, String


class User(db.Model):
  __tablename__ = 'tb_user'
  id = Column('id', Integer, primary_key = True, autoincrement= True), 
  name = Column('name', String), 
  last_name = Column('last_name', String), 
  user = Column('user', String), 
  password = Column('password', String), 
)
