from unittest.mock import MagicMock
from flaskr.resources.drive_list_files import GoogleDrive

def test_list_files_success(monkeypatch):
    mock_get_creds = MagicMock(return_value={"message": "Conexão realizada com sucesso!"})
    monkeypatch.setattr("flaskr.resources.drive_list_files.GoogleDrive.get_creds", mock_get_creds)

    monkeypatch.setattr("flaskr.cloud.drive.GoogleDrive.get_folder_id_by_name", lambda x, y: "folder_id")
    monkeypatch.setattr("flaskr.cloud.drive.build", MagicMock())
    monkeypatch.setattr("builtins.open", MagicMock())
    monkeypatch.setattr("json.load", MagicMock())

    gd = GoogleDrive()
    gd.credentials = True  

    result = gd.list_files()

    assert "files" in result
