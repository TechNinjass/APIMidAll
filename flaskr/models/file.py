from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from io import BytesIO
from googleapiclient.http import MediaIoBaseDownload


from flaskr.cloud_connection.drive_connection import get_creds

from flaskr.db import db_instance

class FileModel(db_instance.Model):
    __tablename__ = 'file'
    
    file_id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)
    size_files = db_instance. Column(db_instance.Integer)
    format_file = db_instance.Column(db_instance.String(30))
    name = db_instance.Column(db_instance.String(254))
    data_upload = db_instance.Column(db_instance.Date, index=True)
    
    # cloud_id = db_instance.Column(db_instance.Integer, db_instance.ForeignKey('cloud.cloud_id'))

    @classmethod
    def get_files_drive(cls):
        try:
            service = build('drive', 'v3', credentials=get_creds())
            print("deu certo a conexão")
            results = service.files().list(
                pageSize=10, fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])

            if not items:
                print('No files found.')
                return []

            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

            return items
        except HttpError as error:
            # TODO(developer) - Handle errors from drive API.
            print(f'An error occurred: {error}')
            return []
    
    @classmethod
    def download_file_drive(cls, file_id):
        try:
            service = build('drive', 'v3', credentials=get_creds())
            file = service.files().get(fileId=file_id).execute()
            file_content = BytesIO()
            downloader = MediaIoBaseDownload(file_content, service.files().get_media(fileId=file_id))
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                # print(f'Download {int(status.progress() * 100)}.')
            file_content.seek(0)
            return file_content.read()
        except HttpError as error:
            # TODO(developer) - Handle errors from drive API.
            print(f'An error occurred: {error}')
