import flaskr.config_app as ca
from flaskr.db import db_instance, db_persist

class FileTransferDeveloperModel(db_instance.Model):
    __bind_key__ = ca.MIDALL_DATABASE_DEVELOPER
    __tablename__ = 'file_transfer_developer'
    __table_args__ =  {"schema": ca.MIDALL_DB_SCHEMA_DEVELOPER}
    
    file_id = db_instance.Column(db_instance.Integer, primary_key=True)
    name = db_instance.Column(db_instance.String(100))
    size = db_instance.Column(db_instance.Integer)
    format = db_instance.Column(db_instance.String(100))
    date_upload = db_instance.Column(db_instance.Date)
    data_transfer = db_instance.Column(db_instance.Date)
    status = db_instance.Column(db_instance.String(100))
    
    @db_persist
    def save(self):
        db_instance.session.merge(self)