from flaskr.db import db_instance

class CloudModel(db_instance.Model):
    __tablename__ = 'cloud'

    cloud_id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)          
    url_cloud_destiny = db_instance.Column(db_instance.String(254))  
    url_cloud_origin = db_instance.Column(db_instance.String(254))       
    secret_key_origin = db_instance.Column(db_instance.String(254), unique=True)          
    secret_key_destiny = db_instance.Column(db_instance.String(254), unique=True)

    configuration_id = db_instance.Column(db_instance.Integer, db_instance.ForeignKey('configuration.config_id'))

    files = db_instance.relationship('FileModel', backref="file")
    network_datas = db_instance.relationship('NetworkDataModel', backref='network_data')