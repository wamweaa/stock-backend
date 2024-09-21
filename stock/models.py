from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, default=1000.0)#starting balance

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    stock_id = db.Column(db.Integer,db.ForeignKey('stock.id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    type = db.Column(db.String(10))