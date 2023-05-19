from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/add_user/Mrinal')
def add_user(name):
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": f"User {name} has been created."}), 201

@app.route('/users')
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({"id": user.id, "name": user.name})
    return jsonify(users_list), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
