from flask import Flask, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:D9XSyvk@localhost:5432/EmployeesCatalog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class EmployeesCatalog(db.Model):
    __tablename__ = 'EmployeesCatalog'
    id = db.Column(db.Integer, primary_key=True)
    lfname = db.Column(db.String(64))
    post = db.Column(db.String(64))
    wages = db.Column(db.Float(8))
    adddate = db.Column(db.String(8))

    def __init__(self, lfname, post, wages, adddate):
        self.lfname = lfname
        self.post = post
        self.wages = wages
        self.adddate = adddate