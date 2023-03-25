from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from flaskr.db import db_instance

from flaskr.models.files import FilesModel
from flaskr.models.network_data import NetworkDataModel


class CloudModel(db_instance.Model):
    __tablename__ = 'cloud'

    cloud_id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)          
    url_cloud_destiny = db_instance.Column(db_instance.String(254))  
    url_cloud_origin = db_instance.Column(db_instance.String(254))       
    secret_key_origin = db_instance.Column(db_instance.String(254))          
    secret_key_destiny = db_instance.Column(db_instance.String(254))       
    configuration_config_id = db_instance.Column(db_instance.Integer, ForeignKey('configuration.config_id'))  
    
    files = relationship(FilesModel, back_populates="cloud")
    networks = relationship(NetworkDataModel, back_populates="cloud")

    __table_args__ = (
        PrimaryKeyConstraint('cloud_id', 'secret_key_origin', 'secret_key_destiny'),
    )
