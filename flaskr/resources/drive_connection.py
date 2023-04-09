from flask import request
from flask_restful import Resource
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from flaskr.cloud.drive import Drive


class GoogleDriveResource(Resource):
    def post(self):


        drive = Drive()
    
        return {"message": "Conexão com o Google Drive estabelecida com sucesso."}, 200
