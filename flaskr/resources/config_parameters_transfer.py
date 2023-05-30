from flask import make_response, request
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import Resource

from flaskr.cloud.config_transfer import get_info_transfer
from flaskr.schemas.config_parameters import ConfigParametersPostSchema
from flaskr.schemas.message import MessageSchema


@doc(description="Config parameters for transfer files", tags=['Transfer'])
@use_kwargs(ConfigParametersPostSchema, location=('json'))
@marshal_with(MessageSchema, code=200)
@marshal_with(MessageSchema, code=400)
class ConfigParametersTransferResource(MethodResource, Resource):
    def post(self, **kwargs):

        hours = int(request.json.get("hours"))
        minutes = int(request.json.get("minutes"))
        folder_drive = request.json.get("folder_drive")
        folder_azure = request.json.get("folder_azure")
        
        parameters = get_info_transfer(hours=hours, minutes=minutes,\
                                       folder_drive=folder_drive, folder_azure=folder_azure)
        
        return make_response({"message": "sucess config!"}, 200)