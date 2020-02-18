from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)
from app.controllers import default

@app.route('/', methods=["POST", "GET"], defaults={"graph": None})
def index(graph):
    return default.padrao()