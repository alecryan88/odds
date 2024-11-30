import boto3    
import json


class awsHandler:

    def __init__(self) -> None:
        self.s3 = boto3.client('s3')

    def upload_json_to_s3(self, json_data: str, bucket: str, file: str) -> None:

        self.s3.put_object(
            Body=json.dumps(json_data),
            Bucket=bucket,
            Key=file,
            ContentType='application/json'
        )
