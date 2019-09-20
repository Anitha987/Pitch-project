from werkzeug.security import generate_password_hash,check_password_hash
from .import db 
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255))
  pass_secure = db.Column(db.String(225))
  pitch_id=db.Column(db.Integer,db.ForeignKey('pitches.id'))
  @property
  def password(self):
      raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
      self.pass_secure = generate_password_hash(password)


  def verify_password(self,password):
      return check_password_hash(self.pass_secure,password)
  def __repr__(self):
    return f'User {self.username}'

class Pitch(db.Model):
  __tablename__ = 'pitches'

  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(255))
  users = db.relationship('User',backref = 'pitch',lazy="dynamic")


  def __repr__(self):
    return f'User {self.name}'

class Category(db.Model): 
  __tablename__= 'categories' 
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String(255))

class Comment(db.Model):
  __tablename__='comments'
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String(225))

class Vote(db.Model):
  __tablename__='votes'
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String(225))

