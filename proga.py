from flask import Flask, render_template
import random

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)

ran = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=True, default='text') 

@app.route("/<id>")
def hello_world(id):
    route = ''.join([ran[random.randint(0, len(ran))] for i in range(10)])
    return "<a href = /" + str(id) + '/' + route + ">Ссылка</a>"

@app.route("/<id>/<route>")
def new(id, route):
    items = Item.query.filter_by(user_id=id).all()
    return render_template('index.html', info=items, user_id=id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')