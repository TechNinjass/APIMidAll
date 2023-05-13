
import pytest 
from flaskr.cloud.azure import Azure
from flaskr.resources.azure_connection import AzureResource


class TestAzureConnection:
   
    def test_connection_azure_happy(self, mocker):
        mock_post = mocker.patch.object(AzureResource, 'post')
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "Conexão realizada com sucesso!"}

        data = {"account_name": "test_account", "account_key": "test_key", "container_name": "test_container"}
        response = AzureResource().post(data=data)

        assert response.status_code == 200
        assert response.json() == {"message": "Conexão realizada com sucesso!"}

       
    def test_connection_azure_edge_file_not_exist(self, mocker):
        mocker.patch('os.path.exists', return_value=False)
        azure = Azure()
        with pytest.raises(Exception):
            azure.connection_azure()        
    
    
    def test_connection_azure_edge(self, mocker):
        mock_azure = mocker.patch("flaskr.cloud.azure.Azure.connection_azure")
        mock_azure.side_effect = Exception("Invalid credentials")

        mock_post = mocker.patch.object(AzureResource, "post")
        mock_post.return_value.status_code = 500
        mock_post.return_value.json = {"error": "Invalid credentials"}

        data = {"account_name": "test_account", "account_key": "test_key"}
        response = AzureResource().post(data=data)

        assert response.status_code == 500
        assert response.json == {"error": "Invalid credentials"}

