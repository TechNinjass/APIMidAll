from flask_restful import Api

from flaskr.resources.azure_connection import AzureResource
from flaskr.resources.azure_list_files import AzureFilesResource
from flaskr.resources.drive_connection import GoogleDriveResource
from flaskr.resources.drive_list_files import GoogleDriveFilesResource
from flaskr.resources.config_parameters_transfer import ConfigParametersTransferResource
from flaskr.resources.file_transfer import FileTransferResource


def config_app_routes(app):
    api = Api(app)
    
    __setting_route_doc(AzureResource, "/azure", api)
    __setting_route_doc(AzureFilesResource, "/azure_files", api)
    __setting_route_doc(GoogleDriveResource, "/drive", api)
    __setting_route_doc(GoogleDriveFilesResource, "/drive_files/", api)
    __setting_route_doc(ConfigParametersTransferResource, "/config_transfer", api)
    __setting_route_doc(FileTransferResource, "/transfer_files", api)
    
    return api

def __setting_route_doc(resource, route, api):
    api.add_resource(resource, route)