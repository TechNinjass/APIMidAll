from marshmallow import fields

from flaskr.schema import ma


class DrivePostSchema(ma.Schema):
    client_id = fields.Str()
    client_secret = fields.Str()

    class Meta:
        #Fields to expose
        fields = ("client_id", "client_secret")
        ordered = True
