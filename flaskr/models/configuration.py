

class Configuration():
    __tablename__ = 'configuration'
    config_id =  db_instance.Column(db_instance.Integer, primary_key=True, index= True)
    limit_size_transfer = (db_instance.Integer)
    limit_size_files_send = (db_instance.Integer)
    time_start_verify = (db_instance.Integer)
    time_end_verify_files = (db_instance.Integer)
    internal_verify_files = (db_instance.Integer)
    date_update =  db_instance.Column(db_instance.Date, index=True)
    path_file_origin = db_instance.Column(db_instance.String(254)) 
    path_file_destiny = db_instance.Column(db_instance.String(254)) 

    cloud = relationship("Cloud", back_populates="configuration")