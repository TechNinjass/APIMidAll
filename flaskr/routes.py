from flask_restful import Api

from flaskr.resources.list_files_aws import AWSResource
from flaskr.resources.file_transfer import FileTransferResource
from flaskr.resources.list_files_drive import GoogleDriveResource

def config_app_routes(app):
    api = Api(app)
    __setting_route_doc(AWSResource, '/aws', api)
    __setting_route_doc(FileTransferResource, '/transfer', api)
    __setting_route_doc(GoogleDriveResource, '/drive', api)
    return api

def __setting_route_doc(resource, route, api):
    api.add_resource(resource, route)
