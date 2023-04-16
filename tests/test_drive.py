# Tests that the function successfully retrieves valid credentials from an existing token file. tags: [happy path]
from flaskr.cloud.drive import GoogleDrive
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from unittest import mock
import pytest


class TestDrive:

        # Tests that get_creds() returns a successful connection message and saves credentials to token.pickle file. 
    def test_get_creds_successful(self, mocker):
        # Arrange
        client_id = "test_client_id"
        client_secret = "test_client_secret"
        flow_mock = mocker.Mock()
        credentials_mock = mocker.Mock()
        flow_mock.run_local_server.return_value = credentials_mock
        InstalledAppFlow.from_client_config.return_value = flow_mock

        # Act
        google_drive = GoogleDrive()
        result = google_drive.get_creds(client_id, client_secret)

        # Assert
        assert result == {"message": "Conexão realizada com sucesso."}
        InstalledAppFlow.from_client_config.assert_called_once_with(
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
        flow_mock.run_local_server.assert_called_once_with(port=0)
        pickle.dump.assert_called_once_with(credentials_mock, mocker.ANY)