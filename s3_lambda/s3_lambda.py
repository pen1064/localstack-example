import logging
import os
from datetime import datetime

import boto3

LOGGER = logging.getLogger()


def handler(event, context):
    boto3.set_stream_logger()
    s3_client = boto3.client(
        "s3",
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name="us-east-1",
        endpoint_url="http://" + os.environ["LOCALSTACK_HOSTNAME"] + ":4566",
    )  # https://github.com/localstack/localstack/issues/2421
    try:
        s3_client.put_object(Bucket="test-bucket", Key="{}".format(datetime.now().isoformat()), Body=event["item"])
        return {"message": "object placed"}
    except:
        return {"message": "object failed placing in s3"}
