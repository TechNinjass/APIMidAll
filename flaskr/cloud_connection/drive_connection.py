import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from io import BytesIO


SCOPES = ['https://www.googleapis.com/auth/drive']

class Drive():

    @classmethod
    def get_files_drive(cls):
        try:
            service = build('drive', 'v3', credentials=get_creds())
            print("Conexão com o Google Drive estabelecida com sucesso.")

            # ID da pasta que você deseja listar os arquivos
            folder_id = '1CVSxS3Tktbz1ugxATpsjG8ZRfBr9ayRp'

            query = f"'{folder_id}' in parents and trashed = false"

            results = service.files().list(
                q=query, pageSize=10, fields="nextPageToken, files(id, name)").execute()

            items = results.get('files', [])

            if not items:
                print('Nenhum arquivo encontrado.')
                return []

            print('Arquivos:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

            return items
        except HttpError as error:
            print(f'Ocorreu um erro: {error}')
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


def get_creds():
        creds = None

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    r'C:\Users\josej\OneDrive\Área de Trabalho\midall-parent\midall-backend\flaskr\cloud_connection\credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return creds

#https://drive.google.com/drive/folders/1zbDbzBJxMHray9uY7bIJQw7viA7YsUmK?usp=share_link