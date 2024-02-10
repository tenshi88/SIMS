from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(os.path.dirname(__file__), "models/sims.db")
app.secret_key = 'super_hyper_ultra_ultimate_secret_key'
db = SQLAlchemy()
db.init_app(app)

from SIMS.views import *