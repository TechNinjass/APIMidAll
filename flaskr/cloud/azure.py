import json
import os.path

from azure.storage.blob import BlobProperties, BlobServiceClient

import flaskr.cloud.set_parameters as sp


class Azure():
    def __init__(self):
        self.account_name = None
        self.account_key = None
        self.container_name = None

    def connection_azure(self, account_name=None, account_key=None, container_name=None, use_json=True):
        if use_json:
            if os.path.exists(sp.AZURE_CREDENTIALS):
                with open(sp.AZURE_CREDENTIALS, "r") as f:
                    credentials = json.load(f)
                if (account_name is None or account_name == credentials["account_name"]) and \
                (account_key is None or account_key == credentials["account_key"]) and \
                (container_name is None or container_name == credentials["container_name"]):
                    connect_str = f'DefaultEndpointsProtocol=https;AccountName={credentials["account_name"]};AccountKey={credentials["account_key"]};EndpointSuffix=core.windows.net'
                    return BlobServiceClient.from_connection_string(connect_str)

            use_json = False

        if account_name is not None and account_key is not None and container_name is not None:
            credentials = {"account_name": account_name, "account_key": account_key, "container_name": container_name}
            with open(sp.AZURE_CREDENTIALS, "w") as f:
                json.dump(credentials, f)

        connect_str = 'DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix=core.windows.net'.format(credentials["account_name"], credentials["account_key"])

        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        return blob_service_client


    def list_files(self):
        with open(sp.AZURE_CREDENTIALS) as f:
            credentials = json.load(f)

        connect_str = f"DefaultEndpointsProtocol=https;AccountName={credentials['account_name']};AccountKey={credentials['account_key']};EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        with open(sp.PARAMETERS_TRANSFER) as f:
            params = json.load(f)
        folder_name = params.get('folder_azure')

        container_name = credentials['container_name']
        container_client = blob_service_client.get_container_client(container_name)

        if folder_name:
            blob_list = container_client.list_blobs(name_starts_with=folder_name)
        else:
            blob_list = container_client.list_blobs()

        files = []
        for blob in blob_list:
            if not blob.name.endswith('/'):
                file = {
                    "name": blob.name,
                    "size": blob.size,
                    "content_type": blob.content_settings.content_type
                }
                files.append(file)

        return files

    def list_folders(self):
        with open(sp.AZURE_CREDENTIALS) as f:
            credentials = json.load(f)

        connect_str = f"DefaultEndpointsProtocol=https;AccountName={credentials['account_name']};AccountKey={credentials['account_key']};EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        container_name = credentials['container_name']
        container_client = blob_service_client.get_container_client(container_name)

        blobs = container_client.walk_blobs(delimiter='/')

        folders = []
        for blob in blobs:
            if blob.name.endswith('/'):
                folder_name = blob.name[:-1]
                folders.append(folder_name)
                print(f"Folder name: {folder_name}")

        return folders
