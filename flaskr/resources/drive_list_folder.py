from flask_restful import Resource

from flaskr.cloud.drive import GoogleDrive


class GoogleDriveFolderResource(Resource):
    def get(self):
        try:
            gd = GoogleDrive()
            folders = gd.list_folders()
            return {"folders": folders}, 200
        except Exception as e:
            return {"error": str(e)}, 500
