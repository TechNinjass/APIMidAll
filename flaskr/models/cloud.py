

class cloud():
    __tablename__ = 'cloud'
    cloud_id = db_instance.Column(db_instance.Integer, primary_key=True, index= True)          
    url_cloud_destiny  = db_instance.Column(db_instance.String(254))  
    url_cloud_origin   = db_instance.Column(db_instance.String(254))       
    secret_key_origin  = db_instance.Column(db_instance.String(254))          
    secret_key_destiny = db_instance.Column(db_instance.String(254))       
    configuration_config_id  = (db_instance.Integer, ForeignKey('configuration.config_id'))  
    
    file = relationship("File", back_populates="cloud")
    network = relationship("network_data", back_populates ="cloud")

    __table_args__ = (
        PrimaryKeyConstraint('cloud_id', 'secret_key_origin','secret_key_destiny'),
    )