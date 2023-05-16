import json
import os
from io import BytesIO

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

import flaskr.cloud.set_parameters as sp


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
            scopes=["https://www.googleapis.com/auth/drive"],
        )

        credentials = flow.run_local_server(port=0, access_type='offline', include_granted_scopes=False)

        with open(sp.DRIVE_CREDENTIALS, "w") as token:
            json.dump({
                "token": credentials.token,
                "refresh_token": credentials.refresh_token,
                "token_uri": credentials.token_uri,
                "client_id": credentials.client_id,
                "client_secret": credentials.client_secret,
                "scopes": credentials.scopes,
            }, token)

        credentials = credentials
        return credentials, {"message": "Conexão realizada com sucesso."}

    def get_folder_id_by_name(drive_client, folder_name):
        query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
        results = drive_client.files().list(q=query, fields="files(id)").execute()
        items = results.get("files", [])
        if items:
            return items[0]["id"]
    
    def list_files(self):
        if not self.credentials:
            if os.path.exists(sp.DRIVE_CREDENTIALS):
                with open(sp.DRIVE_CREDENTIALS, "r") as token:
                    creds_dict = json.load(token)
                    self.credentials = Credentials.from_authorized_user_info(info=creds_dict)
            else:
                return {
                    "error": "As credenciais do Google Drive não foram encontradas."
                }

        try:
            drive_client = build("drive", "v3", credentials=self.credentials)

            with open(sp.PARAMETERS_TRANSFER, "r") as f:
                data = json.load(f)
            folder_name = data["folder_drive"]
            
            folder_id = None
            if folder_name:
                folder_id = GoogleDrive.get_folder_id_by_name(drive_client, folder_name)
                if not folder_id:
                    return {"error": f"A pasta '{folder_name}' não foi encontrada."}

            files = []
            results = drive_client.files().list(
                q=f"'{folder_id}' in parents",
                pageSize=10,
                fields="nextPageToken, files(id, name)"
            ).execute()

            items = results.get("files", [])

            if not items:
                return {"message": "Nenhum arquivo encontrado."}

            for item in items:
                files.append(f"{item['name']} ({item['id']})")

            return {"files": files}

        except HttpError as error:
            return {"error": f"Ocorreu um erro ao listar os arquivos: {error}"}

        
    def list_folders(self):
        if not self.credentials:
            if os.path.exists(sp.DRIVE_CREDENTIALS):
                with open(sp.DRIVE_CREDENTIALS, "r") as token:
                    creds_dict = json.load(token)
                    self.credentials = Credentials.from_authorized_user_info(info=creds_dict)
            else:
                return {
                    "error": "As credenciais do Google Drive não foram encontradas."
                }
        try:
            drive_client = build("drive", "v3", credentials=self.credentials)
            folders = []
            results = drive_client.files().list(
                q="mimeType='application/vnd.google-apps.folder'",
                pageSize=10,
                fields="nextPageToken, files(id, name)"
            ).execute()
            items = results.get("files", [])

            if not items:
                return {"message": "Nenhuma pasta encontrada."}

            for item in items:
                folders.append(f"{item['name']}")

            return {"folders": folders}

        except HttpError as error:
            return {"error": f"Ocorreu um erro ao listar as pastas: {error}"}


    def download_file(self, file_id):
        if not self.credentials:
            if os.path.exists(sp.DRIVE_CREDENTIALS):
                with open(sp.DRIVE_CREDENTIALS, "r") as token:
                    self.credentials = Credentials.from_authorized_user_info(info=json.load(token))
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

    def remove_files(self, file_id):
        if not self.credentials:
            if os.path.exists(sp.DRIVE_CREDENTIALS):
                with open(sp.DRIVE_CREDENTIALS, "r") as token:
                    self.credentials = json.load(token)
            else:
                return {
                    "error": "As credenciais do Google Drive não foram encontradas."
                }

        service = build('drive', 'v3', credentials=self.credentials)

        try:
            service.files().delete(fileId=file_id).execute()
            print(f'O arquivo com ID {file_id} foi excluído com sucesso!')
        except HttpError as error:
            print(f'Ocorreu um erro: {error}')
