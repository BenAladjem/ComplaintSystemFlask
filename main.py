from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from db import db

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
api = Api(app)
migrate = Migrate(app, db)

[api.add_resource(*route_data) for route_data in routes]

db.init_app(app)

if __name__ == "__main__":
    app.run()