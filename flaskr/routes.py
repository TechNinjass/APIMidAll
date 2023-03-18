from flask_restful import Api
from flaskr.resources.google_drive import GoogleDriveResource
from flaskr.resources.dropbox import DropboxResource
def config_app_routes(app):
    api = Api(app)
    __setting_route_doc(GoogleDriveResource, '/drive', api)
    __setting_route_doc(DropboxResource, '/drop', api)
    return api

def __setting_route_doc(resource, route, api):
    api.add_resource(resource, route)
