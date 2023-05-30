from marshmallow import fields

from flaskr.schema import ma


class AzurePostSchema(ma.Schema):
    account_name = fields.Str()
    account_key = fields.Str()
    container_name = fields.Str()

    class Meta:
        #Fields to expose
        fields = ("account_name", "account_key","container_name")
        ordered = True
