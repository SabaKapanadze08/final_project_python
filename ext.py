from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdasdasfgasgas12"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['UPLOAD_FOLDER'] = '/static'

db = SQLAlchemy(app)
login_manager = LoginManager(app)