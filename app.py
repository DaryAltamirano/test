from flask import Flask
from routes.routes import register
from models.index import DATABASE_CONNECTION_URI
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI

register(app)
