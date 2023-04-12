from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from io import BytesIO
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = ['https://www.googleapis.com/auth/drive']

class Drive:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_files_drive(self):
        try:
            creds = get_creds(self.client_id, self.client_secret)
            service = build('drive', 'v3', credentials=creds)
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

    # def download_file_drive(self, file_id):
    #     try:
    #         service = build('drive', 'v3', credentials=self.creds)
    #         file = service.files().get(fileId=file_id).execute()
    #         file_content = BytesIO()
    #         downloader = MediaIoBaseDownload(file_content, service.files().get_media(fileId=file_id))
    #         done = False
    #         while done is False:
    #             status, done = downloader.next_chunk()
    #             # print(f'Download {int(status.progress() * 100)}.')
    #         file_content.seek(0)
    #         return bytes(file_content.getvalue())
    #     except HttpError as error:
    #         # TODO(developer) - Handle errors from drive API.
    #         print(f'An error occurred: {error}')



def get_creds(client_id, client_secret):

    flow = InstalledAppFlow.from_client_config({
        'installed': {
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uris': ['http://localhost'],
            'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
            'token_uri': 'https://oauth2.googleapis.com/token',
            'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
            'client_type': 'installed'
        }
    }, scopes=SCOPES)

    creds = flow.run_local_server(port=0)
    return creds