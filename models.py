from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import DateTime, func

db = SQLAlchemy()

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, unique=True, nullable=False)
	username = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, unique=False, nullable=False)
	posts = db.relationship('Posts', backref='author', lazy='dynamic')
	profile = db.relationship('Profile', backref='author', uselist=False)

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	title = db.Column(db.String(1000), nullable=False) # Added this line
	content = db.Column(db.String(1000), nullable=False)
	image_name = db.Column(db.String(255))  # Store the path to the uploaded image
	timestamp = db.Column(DateTime(timezone=True), default=func.now())
	
class Profile(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
	background_color = db.Column(db.String(1000), default="#FFFFFF") 
	hover_color = db.Column(db.String(1000), default="#cccccc")
	social_media_accounts = db.relationship('SocialMediaAccount', backref='user', lazy='dynamic')

class SocialMediaAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    platform = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	content = db.Column(db.String(1000), nullable=False)
	timestamp = db.Column(DateTime(timezone=True), default=func.now())