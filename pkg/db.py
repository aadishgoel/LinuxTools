from config.config import *

class S3:
    def __init__(self, bucket):
        self.client = boto3.resource("s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY )
        self.bucket = client.Bucket(BUCKET_NAME)
