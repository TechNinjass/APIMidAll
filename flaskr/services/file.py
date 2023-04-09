from flaskr.cloud.aws import connect_to_s3
from flaskr.cloud.drive import Drive
from boto3 import *
 
class FileModelService:
    def __init__(self):
        self.file_model = Drive()

    def transfer_files(self):
        s3, bucket_name = connect_to_s3()
        files_drive = Drive.get_files_drive()

        for item in files_drive:
            file_name = item['name']
            file_id = item['id']
            file_content = self.file_model.download_file_drive(file_id)
            if file_content is not None:
                s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
            else:
                print(f"O arquivo {file_name} não foi baixado com sucesso.")


        print(f"{len(files_drive)} arquivos foram transferidos para o S3 com sucesso.")
