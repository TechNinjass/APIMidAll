from marshmallow import fields

from flaskr.schema import ma


class ConfigParametersPostSchema(ma.Schema):
    hours = fields.Int()
    minutes = fields.Int()
    folder_drive = fields.Str()
    folder_azure = fields.Str()

    class Meta:
        #Fields to expose
        fields = ("hours", "minutes","folder_drive","folder_azure")
        ordered = True
