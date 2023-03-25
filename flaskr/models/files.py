
class Files():
    __tablename__ = 'files'
    file_id =  db_instance.Column(db_instance.Integer, primary_key=True, index= True)
    size_files = db_instance.Column(db_instance.Integer)
    format_file = db_instance.Column(db_instance.String(30))
    name = db_instance.Column(db_instance.String(254))
    data_upload = db_instance.Column(db_instance.Date, index=True)
    cloud_cloud_id = db_instance.Column(db_instance.Integer, ForeignKey('cloud.id'))
    cloud_secret_key_origin =  db_instance.Column(db_instance.String(254),ForeignKey('cloud.secret_key_origin'))
    cloud_secret_key_destiny =  db_instance.Column(db_instance.String(254),ForeignKey('cloud.secret_key_destiny'))
    
   