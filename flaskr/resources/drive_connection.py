from flask import request
from flask_restful import Resource

from flaskr.cloud.drive import get_creds

class GoogleDriveResource(Resource):
    def post(self):
        client_id = request.json.get("client_id")
        client_secret = request.json.get("client_secret")

        con = get_creds(client_id=client_id,
                            client_secret=client_secret)
        return con