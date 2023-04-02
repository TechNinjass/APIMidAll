import boto3

def connect_to_s3():

    aws_access_key_id = 'AKIA2J3TPQFIR4MWOGQO'
    aws_secret_access_key = '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'
    
    bucket_name = 'techninja'

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    return s3, bucket_name

