from flask import Flask

from flaskr.db import config_sql_alchemy, db_instance
from flaskr.migrate import load_migrate
from flaskr.routes import config_app_routes

app = Flask(__name__)

# Config SQLAlchemy
config_sql_alchemy(app)

# Config Flask Restful
api = config_app_routes(app)

# Load Flask Migrate
migrate = load_migrate(db_instance, app)

if __name__ == '__main__':
    app.run()
