import pytest
from unittest.mock import MagicMock

from flaskr.resources.azure_list_files import AzureFilesResource

class TestAzureListFiles:
    
    def test_list_folders(self, mocker):
        azure_mock = mocker.Mock()
        azure_mock.list_folders.return_value = ["folder1", "folder2"]
        mocker.patch('flaskr.cloud.azure.Azure', return_value=azure_mock)

        get_mock = mocker.patch.object(AzureFilesResource, 'get')
        get_mock.return_value = ({"folders": ["folder1", "folder2"]}, 200)

        response = AzureFilesResource().get()

        assert response[0]["folders"] == ["folder1", "folder2"]
        assert response[1] == 200


    