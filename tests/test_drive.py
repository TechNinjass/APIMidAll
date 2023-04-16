# Tests that the function successfully retrieves valid credentials from an existing token file. tags: [happy path]
from flaskr.cloud.drive import GoogleDrive
from pytest_mock import mocker
import pytest


class TestDrive:

    def test_list_files_no_files_found(self, mocker):
        # Setup
        mock_credentials = mocker.Mock()
        mock_build = mocker.patch("googleapiclient.discovery.build")
        mock_build.return_value.files.return_value().list.return_value.execute.return_value = {
            "files": []
        }
        google_drive = GoogleDrive()
        google_drive.credentials = mock_credentials

        result = google_drive.list_files()

        assert "message" in result
        assert result["message"] == "Nenhum arquivo encontrado."


    def test_download_file_successful(self, mocker):
        # Setup
        mock_credentials = mocker.Mock()
        mock_build = mocker.patch("googleapiclient.discovery.build")
        mock_build.return_value.files.return_value().get.return_value.execute.return_value = {
            "id": "123",
            "name": "test_file",
            "mimeType": "text/plain"
        }
        mock_downloader = mocker.Mock()
        mock_downloader.next_chunk.return_value = (None, True)
        mock_media = mocker.Mock()
        mock_media.get.return_value = mock_downloader
        mock_drive_client = mocker.Mock()
        mock_drive_client.files.return_value().get_media.return_value = mock_media
        mock_build.return_value = mock_drive_client
        google_drive = GoogleDrive()
        google_drive.credentials = mock_credentials

        result = google_drive.download_file("123")

        assert result == b''