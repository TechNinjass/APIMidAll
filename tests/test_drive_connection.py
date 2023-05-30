from unittest.mock import MagicMock
from flaskr.resources.drive_connection import GoogleDriveResource

def test_get_creds_success(mocker):
    mock_request = MagicMock()
    mock_request.json.get.return_value = {
        "client_id": "mock_client_id",
        "client_secret": "mock_client_secret"
    }
    mocker.patch("flaskr.resources.drive_connection.request", mock_request)

    mock_get_creds = mocker.patch("flaskr.resources.drive_connection.GoogleDrive.get_creds")
    mock_get_creds.return_value = {"message": "Conexão realizada com sucesso!"}, 200

    assert  {"message": "Conexão realizada com sucesso!"}
