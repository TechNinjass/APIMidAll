from flask_restful import Resource

from flaskr.cloud.azure import Azure


class AzureFolderResource(Resource):
    def get(self):
        try:
            azure = Azure()
            folders = azure.list_folders()
            return {"folders": folders}, 200
        except Exception as e:
            return {"error": str(e)}, 500