from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# https://qiita.com/KI1208/items/2581ed6f211a2d73e5fd
# より以下を付け足す
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object('flaskr.config')

db = SQLAlchemy(app)

import flaskr.views