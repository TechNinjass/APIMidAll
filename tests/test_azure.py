from flaskr.db import db_instance
from flaskr.models.file_transfer import FileTransferModel
from flaskr.cloud.azure import Azure
import pytest

class TestAzure:
    def test_save_new_file_transfer(self, mocker):
        mock_session = mocker.Mock()
        mocker.patch.object(db_instance, "session", mock_session)
        file_transfer = FileTransferModel(
            name="test_file",
            size=100,
            format="pdf",
            date_upload="2022-01-01",
            data_transfer="2022-01-02",
            status = 'ok'
        )
        file_transfer.save()
        mock_session.merge.assert_called_once_with(file_transfer)
        mock_session.commit.assert_called_once()
 
    def test_connection_azure_invalid_credentials_file(self, mocker):
        mocker.patch('os.path.exists', return_value=False)

        azure = Azure()
        with pytest.raises(Exception):
            azure.connection_azure()
