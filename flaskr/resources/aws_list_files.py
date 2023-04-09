from flask_restful import Resource
from flaskr.cloud.aws import connect_to_s3


class AWSFilesResource(Resource):
    def get(self):
        s3, bucket_name = connect_to_s3()

        objects = s3.list_objects_v2(Bucket=bucket_name)

        print(f'Arquivos no bucket {bucket_name}:')
        if 'Contents' in objects:
            for obj in objects['Contents']:
                print(f'  {obj["Key"]}')
                obj['LastModified'] = obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S')
        else:
            print("Sem item")
    
        return objects
