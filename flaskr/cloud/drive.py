import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from io import BytesIO


class GoogleDrive:
    def __init__(self):
        self.credentials = None

    def get_creds(client_id, client_secret):
        flow = InstalledAppFlow.from_client_config(
            {
                "installed": {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"],
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                }
            },
            scopes=["https://www.googleapis.com/auth/drive.metadata.readonly"],
        )

        credentials = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)

        credentials = credentials

        return {"message": "Conexão realizada com sucesso."}

    def list_files(self):
        if not self.credentials:
            if os.path.exists("token.pickle"):
                with open("token.pickle", "rb") as token:
                    self.credentials = pickle.load(token)
            else:
                return {
                    "error": "As credenciais do Google Drive não foram encontradas."
                }
        try:
            drive_client = build("drive", "v3", credentials=self.credentials)
            files = []
            results = (
                drive_client.files()
                .list(pageSize=10, fields="nextPageToken, files(id, name)")
                .execute()
            )
            items = results.get("files", [])

            if not items:
                return {"message": "Nenhum arquivo encontrado."}

            for item in items:
                files.append(f"{item['name']} ({item['id']})")

            return {"files": files}

        except HttpError as error:
            return {"error": f"Ocorreu um erro ao listar os arquivos: {error}"}
        
    def download_file(self, file_id):
        if not self.credentials:
            if os.path.exists("token.pickle"):
                with open("token.pickle", "rb") as token:
                    self.credentials = pickle.load(token)
            else:
                return {
                    "error": "As credenciais do Google Drive não foram encontradas."
                }
        try:
            drive_client = build("drive", "v3", credentials=self.credentials)
            file = drive_client.files().get(fileId=file_id).execute()
            file_content = BytesIO()
            downloader = MediaIoBaseDownload(file_content, drive_client.files().get_media(fileId=file_id))
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                # print(f'Download {int(status.progress() * 100)}.')
            file_content.seek(0)
            return file_content.read()
        except HttpError as error:
            return {"error": f"Ocorreu um erro ao baixar o arquivo: {error}"}

