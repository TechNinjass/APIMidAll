import os
import pickle

from azure.storage.blob import BlobServiceClient


class Azure:
    def __init__(self):
        self.account_name = None
        self.account_key = None
        self.container_name = None

    def connection_azure(self, account_name=None, account_key=None, container_name=None, use_pickle=False):
        self.account_name = account_name
        self.account_key = account_key
        self.container_name = container_name

        if use_pickle and os.path.exists("credentials.pickle"):
            with open("credentials.pickle", "rb") as f:
                credentials = pickle.load(f)
                self.account_name = credentials["account_name"]
                self.account_key = credentials["account_key"]
                self.container_name = credentials["container_name"]

        connect_str = f"DefaultEndpointsProtocol=https;AccountName={self.account_name};AccountKey={self.account_key};EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        if not use_pickle:
            credentials = {"account_name": self.account_name, "account_key": self.account_key, "container_name": self.container_name}
            with open("credentials.pickle", "wb") as f:
                pickle.dump(credentials, f)

        return blob_service_client

    def list_files(self):
        with open("credentials.pickle", "rb") as f:
            credentials = pickle.load(f)

        connect_str = f"DefaultEndpointsProtocol=https;AccountName={credentials['midall']};AccountKey={credentials['cqsL62aBQBuMSh3Ay2v31fE+CoZHGA4qRiwvizaTRgKmw8bRK4oLL2kyzwm3o89V61K6qOuhFvHQ+AStme6swA==']};EndpointSuffix=core.windows.net"

        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        container_client = blob_service_client.get_container_client(credentials['midall'])

        blob_list = container_client.list_blobs()

        for blob in blob_list:
            print(blob.name)
