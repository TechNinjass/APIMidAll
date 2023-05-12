from flask import request
from flask_restful import Resource

from flaskr.cloud.config_transfer import get_info_transfer
class ConfigParametersTransferResource(Resource):
    def post(self):

        hours = request.json.get("hours")
        minutes = request.json.get("minutes")
        folder_drive = request.json.get("folder_drive")
        folder_azure = request.json.get("folder_azure")
        
        parameters = get_info_transfer(hours=hours, minutes=minutes,\
                                       folder_drive=folder_drive, folder_azure=folder_azure)
        return parameters