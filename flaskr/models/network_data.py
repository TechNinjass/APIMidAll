

class Network_data():
    __tablename__ = 'network_data'
    network_id = db_instance.Column(db_instance.Integer, primary_key=True, index= True)
    speed_upload = db_instance.Column(db_instance.Integer)
    data_used = db_instance.Column(db_instance.Integer)
    size_files_transfer = db_instance.Column(db_instance.Integer)
    time_tranfer = db_instance.Column(db_instance.Integer)
    date_transfer =  db_instance.Column(db_instance.Date, index=True)
    cloud_cloud_id = db_instance.Column(db_instance.Integer, ForeignKey('cloud.id'))
    cloud_secret_key_origin =  db_instance.Column(db_instance.String(254),ForeignKey('cloud.secret_key_origin'))
    cloud_secret_key_destiny =  db_instance.Column(db_instance.String(254),ForeignKey('cloud.secret_key_destiny'))
   
   