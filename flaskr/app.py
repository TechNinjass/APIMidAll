from flask import Flask
from flask_cors import CORS

from flaskr.routes import config_app_routes
# from flaskr.job_scheduler import init_apscheduler

app = Flask(__name__)

# Config CORS
CORS(app)

# Config Flask Restful
api = config_app_routes(app)

# Scheduled_job
# init_apscheduler(app, False)

if __name__ == '__main__':
    app.run()
