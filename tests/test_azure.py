from flaskr.db import db_instance
from flaskr.models.file_transfer import FileTransferModel
from flaskr.cloud.azure import Azure

class TestAzure:

    def test_save_new_file_transfer(self, mocker):
        mock_session = mocker.Mock()
        mocker.patch.object(db_instance, 'session', mock_session)
        file_transfer = FileTransferModel(name='test_file', size=100, format='pdf', date_upload='2022-01-01', data_transfer='2022-01-02')
        file_transfer.save()
        mock_session.merge.assert_called_once_with(file_transfer)
        mock_session.commit.assert_called_once()

    def test_list_files_empty_container(self, mocker):
        mock_blob_service_client = mocker.Mock()
        mock_container_client = mocker.Mock()
        mock_blob_service_client.get_container_client.return_value = mock_container_client
        mocker.patch("azure.storage.blob.BlobServiceClient.from_connection_string", return_value=mock_blob_service_client)

        mock_blob_list = []
        mock_container_client.list_blobs.return_value = mock_blob_list

        azure = Azure()
        files = azure.list_files()

        assert files == []
