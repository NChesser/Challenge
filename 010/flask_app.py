from flask import Flask, render_template, request
from crypto import get_coins, get_coin
from monopoly_odds import get_odds
from collections import namedtuple
from get_search_image import get_search_image
from config import Config

# external
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# login form modules
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

@app.route("/")
@app.route('/', methods=['POST'])
def crypto():
    coins = get_coins()
    if request.method == 'POST':
        coin = request.form.get('coin')
        coins = get_coin(coin)

    return render_template("crypto.html", 
                            links=LINKS, 
                            title="Crypto Prices", 
                            coins=coins)

@app.route('/monopoly')
def monopoly():
    return render_template("monopoly.html", 
                            links=LINKS, 
                            title="Monopoly Odds", 
                            squares=get_odds())

@app.route('/dogs')
def dogs():
    return render_template("dogs.html", 
                            links=LINKS, 
                            title="Dog Breeds", 
                            images=get_search_image('dog'))
	
if __name__ == "__main__":
	app.run()