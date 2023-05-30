from flask import make_response
from flask_apispec import doc, marshal_with
from flask_apispec.views import MethodResource
from flask_restful import Resource

from flaskr.schemas.message import MessageSchema
from flaskr.services.file import FileModelService


@doc(description="Transfer files", tags=['Transfer'])
@marshal_with(MessageSchema, code=200)
class FileTransferResource(MethodResource, Resource):
    def post(self, **kwargs):
        
        file_service = FileModelService()
        file_service.transfer_files()
        return make_response({'message': 'Files transferred successfully'}, 200)
