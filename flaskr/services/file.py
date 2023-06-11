import json
import time
from datetime import datetime

import plyer
from azure.core.exceptions import AzureError

import flaskr.cloud.set_parameters as sp
from flaskr.cloud.azure import Azure
from flaskr.cloud.drive import GoogleDrive
from flaskr.models.file_transfer import FileTransferModel


class FileModelService:
    def __init__(self):
        self.google_drive = GoogleDrive()
        self.azure = Azure()
        self.transfer_size = 0

    def transfer_files(self):
        container_client = self.azure.connection_azure(use_json=True)
        files_drive = self.google_drive.list_files().get('files')

        if not files_drive:
            print("Nenhum arquivo encontrado no Google Drive.")
            return

        with open(sp.PARAMETERS_TRANSFER) as f:
            params = json.load(f)
        folder_name = params.get('folder_azure')
        bandwidth_limit = params.get('bandwidth_limit')

        for item in files_drive:
            if self.transfer_size >= bandwidth_limit:
                print("Limite de banda atingido. A transferência será interrompida até o próximo ciclo.")
                break
            time.sleep(0.5)
            file_name = item.split("(")[0].strip()
            file_id = item.split("(")[1].replace(")", "")
            file_content = self.google_drive.download_file(file_id)

            if not isinstance(file_content, bytes):
                file_content = bytes(str(file_content), 'utf-8')

            transfer = FileTransferModel()
            transfer.name = file_name
            transfer.size = len(file_content)
            transfer.format = file_name.split(".")[-1]
            transfer.date_upload = datetime.now()
            transfer.data_transfer = datetime.now()
            
            blob_path = f"{folder_name}/{file_name}" if folder_name else file_name
            
            if blob_path != None:
                blob_client = container_client.get_blob_client(container='midall', blob=blob_path)
            else:
                blob_client = container_client.get_blob_client(container='midall', blob=file_name)
            try:
                blob_client.upload_blob(file_content, overwrite=True)
                print(f"Arquivo {file_name} transferido com sucesso para o Azure Blob Storage!")
                self.google_drive.remove_files(file_id)
                print(f"Arquivo {file_name} deletado do Google Drive!")
                transfer.status = 'transferido'
                plyer.notification.notify(
                    title='Transferência Concluída',
                    message=f'Arquivo "{file_name}" foi transferido com sucesso para o Azure Blob Storage!',
                    app_name='Midall Transfer',
                    timeout=5
                )
                self.transfer_size += transfer.size
                print(self.transfer_size)
            except AzureError as ex:
                print('Um erro ocorreu durante o upload do arquivo: {}'.format(ex))
                transfer.status = 'erro: {}'.format(str(ex))
                plyer.notification.notify(
                    title='Ocorreu um erro ao transferir',
                    message=f'Arquivo "{file_name}" não foi transferido!',
                    app_name='Midall Transfer',
                    timeout=5
                )
            transfer.save()

            if not isinstance(file_content, bytes):
                file_content = bytes(str(file_content), 'utf-8')
