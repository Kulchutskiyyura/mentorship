from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "host": "mongodb://localhost:27017/reports",
}
db = MongoEngine(app)

import application.server.controllers
