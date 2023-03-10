from flask import Flask

from flaskr.routes import config_app_routes

app = Flask(__name__)

api = config_app_routes(app)

if __name__ == '__main__':
    app.run()
