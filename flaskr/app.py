from flask import Flask
from flask_cors import CORS

from flaskr.db import config_sql_alchemy, db_instance
from flaskr.job_scheduler import init_apscheduler
from flaskr.migrate import load_migrate
from flaskr.migration_developer import migrate_data
from flaskr.routes import config_app_routes
from flaskr.swagger_docs import config_swagger

app = Flask(__name__)

app.config['BUNDLE_ERRORS'] = True
# Config CORS
CORS(app)

# config SQLAlchemy 
config_sql_alchemy(app)

# Migrate data in database developer
migrate_data()

docs = config_swagger(app)

# Config Flask Restful
api = config_app_routes(app, docs)

# Load Flask Migrate
migrate = load_migrate(db_instance, app)

# Scheduled_job
init_apscheduler(app, False, 'task_transfer_files')

if __name__ == '__main__':
    app.run()