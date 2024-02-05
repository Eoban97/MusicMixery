from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret'  # adjust this later

db = SQLAlchemy(app)


@app.route('/')
def main():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=6020)
