from flask_restful import Resource
from flaskr.cloud_connection.drive_connection import Drive
class GoogleDriveResource(Resource):

    def get(self):
        items = Drive.get_files_drive()
        
        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

        return items
