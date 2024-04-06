from config.config import *
import boto3
from abc import abstractmethod
class IFileStore:
    @abstractmethod
    def getFiles(self):
        pass
    @abstractmethod
    def getFile(self, fileObj):
        pass

class AWSFileStore(IFileStore):
    def __init__(self):
        self.client = boto3.resource("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY )
        self.bucket = self.client.Bucket(AWS_BUCKET_NAME)

    def getFiles(self):
        keys = []
        for obj in self.bucket.objects.all():
            keys += [ obj ]
        return keys
    
    def getFile(self, fileObj):
        object = fileObj.get()
        data = object['Body'].read().decode('utf-8')
        return data.split('\n')


