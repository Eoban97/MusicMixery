from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from bcrypt import Bcrypt


app = Flask(__name__)
Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret'  # adjust this later

db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(820), nullable=False)


@app.route('/')
def main():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=6020)
