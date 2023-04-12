from flask import request
from flask_restful import Resource

from flaskr.cloud.drive import get_creds
from flaskr.resources.drive_list_files import GoogleDriveFilesResource

class GoogleDriveResource(Resource):
    def post(self):
        client_id = request.json.get("client_id")
        client_secret = request.json.get("client_secret")

        files_resource = GoogleDriveFilesResource(client_id=client_id, client_secret=client_secret)
        return files_resource.get()

