import boto3
s3_obj = boto3.resource('s3')
print(dir(s3_obj))