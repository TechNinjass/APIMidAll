from flask import request
from flask_restful import Resource

from flaskr.cloud.drive import GoogleDrive


class GoogleDriveResource(Resource):
    def post(self):
        client_id = request.json.get("client_id")
        client_secret = request.json.get("client_secret")

        try:
            creds = GoogleDrive.get_creds(client_id, client_secret)
            return {"message": "Conexão realizada com sucesso!"}, 200

        except Exception as e:
            return {"error": str(e)}, 500
