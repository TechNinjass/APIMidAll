from flaskr.db import db_instance

class FileModel(db_instance.Model):
    __tablename__ = 'file'
    
    file_id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)
    size_files = db_instance. Column(db_instance.Integer)
    format_file = db_instance.Column(db_instance.String(30))
    name = db_instance.Column(db_instance.String(254))
    data_upload = db_instance.Column(db_instance.Date, index=True)
    
    cloud_id = db_instance.Column(db_instance.Integer, db_instance.ForeignKey('cloud.cloud_id'))
