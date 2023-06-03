from flask import make_response, request
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import Resource

from flaskr.cloud.azure import Azure
from flaskr.schemas.azure import AzurePostSchema
from flaskr.schemas.message import MessageSchema


@doc(description="Connection in Azure", tags=['Azure'])
@use_kwargs(AzurePostSchema, location=('json'))
@marshal_with(MessageSchema, code=200)
@marshal_with(MessageSchema, code=400)
class AzureResource(MethodResource, Resource):
    def post(self, **kwargs):
        account_name = request.json.get("account_name")
        account_key = request.json.get("account_key")
        container_name = request.json.get("container_name")

        try:
            azure = Azure()
            creds = azure.connection_azure(account_name, account_key, container_name)
            return make_response({"message": "Conexão realizada com sucesso!"}, 200)

        except Exception as e:
            return make_response({"error": str(e)}, 400)