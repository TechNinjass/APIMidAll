from flask_restful import Api
from flaskr.resources.google_drive import HomeResource

def config_app_routes(app):
    api = Api(app)
    __setting_route_doc(HomeResource, '/home', api)
    return api

def __setting_route_doc(resource, route, api):
    api.add_resource(resource, route)
