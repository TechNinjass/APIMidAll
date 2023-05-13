
from flaskr.cloud.drive import GoogleDrive

class TestDrive:
    def test_list_files_successful(self, mocker):
        mock_creds = mocker.Mock()
        mock_build = mocker.Mock()
        mocker.patch.object(GoogleDrive, 'list_files', return_value={"files": ["test_file (123)"]})
        
        gd = GoogleDrive()
        gd.credentials = mock_creds
        mocker.patch('googleapiclient.discovery.build', return_value=mock_build)
        result = gd.list_files()

        assert result == {"files": ["test_file (123)"]}


    def test_list_files_no_files_found(self, mocker):
        mock_creds = mocker.Mock()
        mock_build = mocker.Mock()
        mocker.patch.object(GoogleDrive, 'list_files', return_value={"message": "Nenhum arquivo encontrado."})
        
        gd = GoogleDrive()
        gd.credentials = mock_creds
        mocker.patch('googleapiclient.discovery.build', return_value=mock_build)
        result = gd.list_files()

        assert result == {"message": "Nenhum arquivo encontrado."}


    def test_download_file_successful(self, mocker):
        mock_creds = mocker.Mock()
        mock_build = mocker.Mock()
        mocker.patch.object(GoogleDrive, 'download_file', return_value=b"test_file_content")
        
        gd = GoogleDrive()
        gd.credentials = mock_creds
        mocker.patch('googleapiclient.discovery.build', return_value=mock_build)
        result = gd.download_file("123")

        assert result == b"test_file_content"
