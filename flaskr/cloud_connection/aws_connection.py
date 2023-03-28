import boto3

def connect_to_s3():

    aws_access_key_id = 'AKIA2J3TPQFIXX7JE56J'
    aws_secret_access_key = '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'
    bucket_name = 'techninja'

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    return s3, bucket_name

