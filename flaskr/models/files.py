from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from flaskr.db import db_instance

class FilesModel(db_instance.Model):
    __tablename__ = 'files'
    
    file_id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)
    size_files = db_instance. Column(db_instance.Integer)
    format_file = db_instance.Column(db_instance.String(30))
    name = db_instance.Column(db_instance.String(254))
    data_upload = db_instance.Column(db_instance.Date, index=True)
    cloud_cloud_id = db_instance.Column(db_instance.Integer, ForeignKey('cloud.cloud_id'))
    cloud = relationship('CloudModel', backref="files")
    cloud_secret_key_origin =  db_instance.Column(db_instance.String(254))
    cloud_secret_key_destiny =  db_instance.Column(db_instance.String(254))
