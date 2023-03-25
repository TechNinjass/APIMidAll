from flaskr.db import db_instance

class NetworkDataModel(db_instance.Model):
    __tablename__ = 'network_data'
    
    network_id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)
    speed_upload = db_instance.Column(db_instance.Integer)
    data_used = db_instance.Column(db_instance.Integer)
    size_files_transfer = db_instance.Column(db_instance.Integer)
    time_tranfer = db_instance.Column(db_instance.Integer)
    date_transfer =  db_instance.Column(db_instance.Date, index=True)

    cloud_id = db_instance.Column(db_instance.Integer, db_instance.ForeignKey('cloud.cloud_id'))

