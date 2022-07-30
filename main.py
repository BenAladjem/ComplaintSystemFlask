from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from db import db

app = Flask(__name__)
ap = Api(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()