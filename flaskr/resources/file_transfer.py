from flask_restful import Resource
from flaskr.services.file import FileModelService

class FileTransferResource(Resource):
    def post(self):
        
        file_service = FileModelService()
        file_service.transfer_files()
        return {'message': 'Files transferred successfully'}, 200
