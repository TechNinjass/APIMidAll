from flaskr.services.file import FileModelService

from flask_restful import Resource



class FileTransferResource(Resource):
    def post(self):
        
        file_service = FileModelService()
        file_service.transfer_files()
        return {'message': 'Files transferred successfully'}, 200
