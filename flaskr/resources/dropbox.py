from flask_restful import Resource
       
from dropbox import DropboxOAuth2Flow
import dropbox


class DropboxResource(Resource):
    def get(self):
            
        dbx = dropbox.Dropbox(
            oauth2_access_token='sl.BazAwUT9E4s7D1qG0FASGrhPAYiwzRbcQBBwZrRbrrLah64xJH-jduZLEdmX59jWbnBsxP9pNzvKJvivoMfl7UlOML9_088UrCqLn0re9MU0qfXp_9l7jrs31CGh_4GZ4EenTMnwsEx-',
            app_key='4k4kxmph890eh78',
            app_secret='64lqv52bd6l64fp'
        )

        files = dbx.files_list_folder('')
        for file in files.entries:
            print(file.name)
        return {'files': file.name}

