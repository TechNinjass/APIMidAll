from flaskr.cloud_connection.aws_connection import connect_to_s3
from flaskr.models.file import FileModel
 
class FileModelService:
    def __init__(self):
        self.file_model = FileModel()

    def transfer_files(self):
        s3, bucket_name = connect_to_s3()
        files_drive = FileModel.get_files_drive()

        for item in files_drive:
            file_name = item['name']
            file_id = item['id']
            file_content = self.file_model.download_file_drive(file_id)
            print(file_id)
            print(file_name)
            print(file_content)
            #s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)

        print(f"{len(files_drive)} arquivos foram transferidos para o S3 com sucesso.")
