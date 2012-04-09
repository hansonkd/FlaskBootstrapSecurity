from flask_application import app

from flaskext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
