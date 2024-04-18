from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# IMPLEMENT LOGIN, PASSWORD_HASHING
class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   firstName = db.Column(db.String(64))
   lastName = db.Column(db.String(64))
   email = db.Column(db.String(120), index=True, unique=True)
   password_hash = db.Column(db.String(64))
   tid = db.Column(db.Integer, db.ForeignKey('Team.id'), index=True)

   def __repr__(self):
       return '<User> {}'.format(self.name)

   def set_password(self, password):
       self.password_hash = generate_password_hash(password)

   def check_password(self, password):
       return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
   return User.query.get(int(id))


class Team(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64))
   Lid = db.Column(db.Integer, db.ForeignKey('League.id'), index=True)
   Pid = db.Column(db.Integer, db.ForeignKey('Player.id'), index=True)

class League(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64))
   Tid = db.Column(db.Integer, db.ForeignKey('Player.id'), index=True)

class Player(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   firstName = db.Column(db.String(64))
   lastName = db.Column(db.String(64))
   avg_score = db.Column(db.Integer, index=True)

class College(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64))
   location = db.Column(db.Integer, db.ForeignKey('location.id'), index=True)


class Location(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64), index=True)
   city = db.Column(db.String(64), index=True)
   state = db.Column(db.String(64), index=True)
   zip = db.Column(db.Integer)
   lat = db.Column(db.Float)
   long = db.Column(db.Float)

   def __repr__(self):
       return '<Location> {}'.format(self.name)

class stat(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   pid = db.Column(db.Integer, db.ForeignKey('Player.id'), index=True)
   score = db.Column(db.Integer)
   week = db.Column(db.Integer)

class user_score(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   uid = db.Column(db.Integer, db.ForeignKey('User.id'), index=True)
   pid = db.Column(db.Integer, db.ForeignKey('Player.id'), index=True)
   wid = db.Column(db.Integer, db.ForeignKey('stat.week'), index=True)
   score = db.Column(db.Integer)

class schedule(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   lid = db.Column(db.Integer, db.ForeignKey('League.id'), index=True)
   htid = db.Column(db.Integer, db.ForeignKey('Team.id'), index=True)
   atid = db.Column(db.Integer, db.ForeignKey('Team.id'), index=True)
   home_score = db.Column(db.Integer)
   ascore = db.Column(db.Integer)
   wid = db.Column(db.Integer, db.ForeignKey('stat.week'), index=True)
   htw = db.Column(db.Boolean)








   

   











