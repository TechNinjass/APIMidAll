from flaskr.cloud.aws import connect_to_s3
from flaskr.cloud.drive import GoogleDrive


class FileModelService:
    def __init__(self):
        self.google_drive = GoogleDrive()

    def transfer_files(self):
        s3, bucket_name = connect_to_s3()
        files_drive = self.google_drive.list_files().get('files')

        if not files_drive:
            print("Nenhum arquivo encontrado no Google Drive.")
            return

        for item in files_drive:
            file_name = item.split("(")[0].strip()
            file_id = item.split("(")[1].replace(")", "")
            file_content = self.google_drive.download_file_drive(file_id)

            if file_content is not None:
                s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
                print(f"O arquivo {file_name} foi transferido com sucesso para o S3.")
            else:
                print(f"O arquivo {file_name} não foi baixado com sucesso do Google Drive.")

        print(f"{len(files_drive)} arquivos foram transferidos com sucesso para o S3.")
