from flaskr.models.file_transfer import FileTransferModel
from flaskr.models.file_transfer_developer import FileTransferDeveloperModel
from flaskr.db import db_instance

def migrate_data():
    with db_instance.app.app_context():
        
        file_transfers = FileTransferModel.query.all()

        for file_transfer in file_transfers:
            
            new_file_transfer = FileTransferDeveloperModel(
                name=file_transfer.name,
                size=file_transfer.size,
                format=file_transfer.format,
                date_upload=file_transfer.date_upload,
                data_transfer=file_transfer.data_transfer,
                status=file_transfer.status
            )

            db_instance.session.add(new_file_transfer)

        db_instance.session.commit()
        print('data migration done')