from flask import make_response
from flask_apispec import doc, marshal_with
from flask_apispec.views import MethodResource
from flask_restful import Resource

from flaskr.cloud.azure import Azure
from flaskr.schemas.message import MessageSchema


@doc(description="List files in blob Azure", tags=['Azure'])
@marshal_with(MessageSchema, code=200)
@marshal_with(MessageSchema, code=500)
class AzureFilesResource(MethodResource, Resource):
    def get(self, **kwargs):
        try:
            azure = Azure()
            files = azure.list_files()
            return make_response({"files": files}, 200)
        except Exception as e:
            return make_response({"error": str(e)}, 500)