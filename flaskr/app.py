from flask import Flask

from flaskr.db import config_sql_alchemy
from flaskr.routes import config_app_routes
from flaskr.job_scheduler import init_apscheduler

app = Flask(__name__)

# Config SQLAlchemy
config_sql_alchemy(app)

# Config Flask Restful
api = config_app_routes(app)

# Scheduled_job
init_apscheduler(app, True)

if __name__ == '__main__':
    app.run()
