from app import db,login_manager
from flask_login import UserMixin
from datetime import datetime

# login handler
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    FirstName = db.Column(db.String())
    LastName = db.Column(db.String())
    username = db.Column(db.String())
    email = db.Column(db.String(100))
    bio = db.Column(db.String())
    role = db.Column(db.String(50)) #Donor, beneficiary, admin
    profile_pic = db.Column(db.String())
    date = db.Column(db.DateTime(), default=datetime.utcnow)


class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String())

class Book(db.Model):
    __tablename__='books'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String())
    publisher = db.Column(db.String())
    author = db.Column(db.String())
    user_id = db.Column(db.String(), db.ForeignKey('users.id')) #donor id
    category_id = db.Column(db.String(), db.ForeignKey('categories.id'))
    date = db.Column(db.DateTime(), default=datetime.utcnow)

class Beneficiary(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(), db.ForeignKey('users.id')) #beneficiary id
    book_id = db.Column(db.String(), db.ForeignKey('books.id')) #book id
    accepted = db.Column(db.Integer) # 0=Not accepted ;1=Accepted
    date = db.Column(db.DateTime(), default=datetime.utcnow)


class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key=True)
    book_id = db.Column(db.String(), db.ForeignKey('books.id'))
    user_id = db.Column(db.String(), db.ForeignKey('users.id'))
    comment = db.Column(db.String())
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    





    
    
