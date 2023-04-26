from flask_restful import Resource

from flaskr.cloud.azure import Azure


class AzureFilesResource(Resource):
    def get(self):
        try:
            azure = Azure()
            files = azure.list_files()
            return {"files": files}, 200
        except Exception as e:
            return {"error": str(e)}, 500