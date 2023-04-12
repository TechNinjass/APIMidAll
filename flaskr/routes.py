from flask_restful import Api

from flaskr.resources.drive_connection import GoogleDriveResource
from flaskr.resources.aws_list_files import AWSFilesResource
from flaskr.resources.file_transfer import FileTransferResource
from flaskr.resources.drive_list_files import GoogleDriveFilesResource


def config_app_routes(app):
    api = Api(app)
    
    __setting_route_doc(GoogleDriveResource, "/drive", api)
    __setting_route_doc(AWSFilesResource, "/aws_files", api)
    __setting_route_doc(FileTransferResource, "/transfer_files", api)
    __setting_route_doc(GoogleDriveFilesResource, "/drive_files/<client_id>/<client_secret>", api)
    
    return api


def __setting_route_doc(resource, route, api):
    api.add_resource(resource, route)
