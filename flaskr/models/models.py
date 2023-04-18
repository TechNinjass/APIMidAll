

from flaskr.db import db_instance

class Files(db_instance.Model):
    File_Id = db_instance.Column(db_instance.Integer, primary_key=True)
    Size_Files = db_instance.Column(db_instance.Integer, nullable=False)
    Format = db_instance.Column(db_instance.String(30), nullable=True)
    Name = db_instance.Column(db_instance.String(254), nullable=False)
    Date_Upload = db_instance.Column(db_instance.Date, nullable=False)
    Clouds_Fk = db_instance.Column(db_instance.Integer, db_instance.ForeignKey('cloud.Cloud_Id'))

class Network_Data(db_instance.Model):
    Network_Id = db_instance.Column(db_instance.Integer, primary_key=True)
    Speed_Upload = db_instance.Column(db_instance.Integer, nullable=False)
    Data_Used = db_instance.Column(db_instance.Date, nullable=False)
    Size_Files_Transf = db_instance.Column(db_instance.Integer, nullable=False)
    Time_Transfer = db_instance.Column(db_instance.Time, nullable=True)
    Data_Transfer = db_instance.Column(db_instance.Date, nullable=True)
    Cloud_Fk = db_instance.Column(db_instance.Integer, db_instance.ForeignKey('cloud.Cloud_Id'))

class Configuration(db_instance.Model):
    Config_Id = db_instance.Column(db_instance.Integer, primary_key=True)
    Limit_Size_Transfer = db_instance.Column(db_instance.Integer, nullable=True)
    Limit_Size_Files_Send = db_instance.Column(db_instance.Integer, nullable=True)
    Time_Start_Verify = db_instance.Column(db_instance.Time, nullable=False)
    Time_End_Verify = db_instance.Column(db_instance.Time, nullable=True)
    Interval_Verify_Files = db_instance.Column(db_instance.Time, nullable=False)
    Date_Update = db_instance.Column(db_instance.Date, nullable=False)
    Path_File_Origin = db_instance.Column(db_instance.String(254), nullable=True)
    Path_File_Destiny = db_instance.Column(db_instance.String(254), nullable=True)
    Cloud_Id = db_instance.Column(db_instance.Integer, db_instance.ForeignKey('cloud.Cloud_Id'), nullable=True)
    cloud = db_instance.relationship('Cloud', backref=db_instance.backref('configurations', lazy=True))

class Cloud(db_instance.Model):
    Cloud_Id = db_instance.Column(db_instance.Integer, primary_key=True)
    Url_Cloud_Destiny = db_instance.Column(db_instance.String(254), nullable=False)
    Url_Cloud_Origin = db_instance.Column(db_instance.String(254), nullable=False)
    Secret_Cloud_Origin = db_instance.Column(db_instance.String(254), nullable=False)
    Secret_Cloud_Destiny = db_instance.Column(db_instance.String(254), nullable=False)
    configurations = db_instance.relationship('Configuration', backref=db_instance.backref('cloud', lazy=True))
    network_data = db_instance.relationship('Network_Data', backref=db_instance.backref('cloud', lazy=True))
    files = db_instance.relationship('Files', backref=db_instance.backref('cloud', lazy=True))



