from flask import jsonify
from flask_restful import Resource

from flaskr.cloud.drive import Drive

class GoogleDriveFilesResource(Resource):
    def __init__(self, client_id, client_secret, **kwargs):
        self.client_id = client_id
        self.client_secret = client_secret
        self.drive = Drive(client_id=self.client_id, client_secret=self.client_secret)
        super().__init__(**kwargs)

    def get(self):
        items = self.drive.get_files_drive()

        if not items:
            print('No files found.')
            return ({'message': 'No files found.'}), 404

        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
        
        return ({'message': 'files found.'}), 200
