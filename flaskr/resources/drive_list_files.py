from flask_restful import Resource
from flaskr.cloud.drive import GoogleDrive


class GoogleDriveFilesResource(Resource):
    def get(self):
        try:
            gd = GoogleDrive()
            files = gd.list_files()
            return {"files": files}, 200
        except Exception as e:
            return {"error": str(e)}, 500
