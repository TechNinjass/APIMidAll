from flask import request
from flask_restful import Resource

from flaskr.cloud.azure import Azure


class AzureResource(Resource):
    def post(self):
        account_name = request.json.get("account_name")
        account_key = request.json.get("account_key")
        container_name = request.json.get("container_name")

        try:
            azure = Azure()
            creds = azure.connection_azure(account_name, account_key, container_name)
            return {"message": "Conexão realizada com sucesso!"}, 200

        except Exception as e:
            return {"error": str(e)}, 500
