from flask_restful import Resource
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from flaskr.cloud_connection.drive_connection import get_creds

class GoogleDriveResource(Resource):

    def get(self):
        try:
            service = build('drive', 'v3', credentials=get_creds())
            results = service.files().list(
                pageSize=10, fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])

            if not items:
                print('No files found.')
                return
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
        except HttpError as error:
            # TODO(developer) - Handle errors from drive API.
            print(f'An error occurred: {error}')

        return items
