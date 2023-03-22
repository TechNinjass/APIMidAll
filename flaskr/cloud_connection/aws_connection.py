import boto3

def connect_to_s3():

    aws_access_key_id = 'AKIAZMGC3PTYETBHHKF6'
    aws_secret_access_key = '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'
    bucket_name = 'tech-ninjas'

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    return s3, bucket_name

