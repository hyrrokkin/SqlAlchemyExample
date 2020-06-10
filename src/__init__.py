from src import config

from flask import Flask

from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

from src import model
