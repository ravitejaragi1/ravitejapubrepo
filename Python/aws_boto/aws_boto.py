import boto3 
import uuid 
s3_client = boto3.client("s3")

s3_resource = boto3.resource('s3')
def create_bucket_name(bucket_prefix) :
    return  ''.join([bucket_prefix, str(uuid.uuid4())])

bucket_name = create_bucket_name("newtest")

s3_resource.create_bucket(Bucket=)

s3_client.delete_bucket(Bucket='newtest92c77138-4c50-445b-a702-758af5cd23c4',)

s3_resource.Object()