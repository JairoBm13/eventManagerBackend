from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_cors import CORS

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import os

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# setup environment and db
load_dotenv(find_dotenv())

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


CORS(
    app,
    supports_credentials=True)



# migrations

@app.cli.command('resetdb')
def create_db():
    """Creates the db tables."""
    db.drop_all()
    db.create_all()

def create_app():
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app