from flask import make_response, request
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import Resource

from flaskr.cloud.drive import GoogleDrive
from flaskr.schemas.drive import DrivePostSchema
from flaskr.schemas.message import MessageSchema


@doc(description="Connection in Drive", tags=['Drive'])
@use_kwargs(DrivePostSchema, location=('json'))
@marshal_with(MessageSchema, code=200)
@marshal_with(MessageSchema, code=400)
class GoogleDriveResource(MethodResource, Resource):
    def post(self, **kwargs):
        client_id = request.json.get("client_id")
        client_secret = request.json.get("client_secret")

        try:
            creds = GoogleDrive.get_creds(client_id, client_secret)
            return make_response({"message": "Conexão realizada com sucesso!", "credentials": creds}, 200)

        except Exception as e:
            return make_response({"error": str(e)}, 500)
