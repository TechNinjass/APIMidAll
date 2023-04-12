from flask_restful import Resource
from flask import jsonify
from flaskr.cloud.drive import Drive
from flaskr.cloud.drive import get_creds


class GoogleDriveFilesResource(Resource):
    def __init__(self):
        self.client_id = None
        self.client_secret = None
        super().__init__()

    def get(self):
        
        if self.client_id is None or self.client_secret is None:
            return {'error': 'client_id and client_secret are required'}, 400

        creds, _, _ = get_creds(self.client_id, self.client_secret)
        drive = Drive(creds, self.client_id, self.client_secret)
        items = drive.get_files_drive()
        
        if not items:
            print('No files found.')
            return {'error': 'no files found'}, 404

        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

        # converte as credenciais em um dicionário e, em seguida, serializa em JSON
        creds_dict = creds.to_json()
        return jsonify({'items': items, 'creds': creds_dict}), 200
