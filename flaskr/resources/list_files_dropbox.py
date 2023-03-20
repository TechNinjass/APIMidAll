from flask_restful import Resource

from flaskr.cloud_connection.dropbox_connection import (create_dbx_client, check_and_refresh_access_token)
                                                
class DropboxResource(Resource):
    def __init__(self):
        #In this line, a new token must be generated if you are running the application for the first time
        #link to get token(https://www.dropbox.com/developers/apps/create)
        self.dbx = create_dbx_client('sl.Ba3yHjFlyKuzrC1Pf9sI_lfAPUVwTg8_HYFVZ83s4lSg8J4PjcTVPGTa0yVaB3OWAPzlmiRHCJutFIMzkx2NajSyQeBNS7ZYc5-E_aDD96OiXfe8S_OLXxBltzIfuSkeMAnRf8N3ZLUN')

    def get(self):
        self.dbx = check_and_refresh_access_token(self.dbx)
        files = self.dbx.files_list_folder('')
        file_names = [file.name for file in files.entries]
        return {'files': file_names}

