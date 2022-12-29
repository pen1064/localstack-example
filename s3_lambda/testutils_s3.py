import json
import os
from zipfile import ZipFile

import boto3
import botocore

CONFIG = botocore.config.Config(retries={"max_attempts": 0})
LAMBDA_ZIP = "./s3_lambda.zip"


def get_lambda_client():
    return boto3.client(
        "lambda",
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name="us-east-1",
        endpoint_url="http://localhost:4566",
        config=CONFIG,
    )


def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name="us-east-1",
        endpoint_url="http://localhost:4566",
    )


def create_lambda_zip(function_name):
    with ZipFile(LAMBDA_ZIP, "w") as z:
        z.write(function_name + ".py")


def create_lambda(function_name):
    lambda_client = get_lambda_client()
    create_lambda_zip(function_name)
    with open(LAMBDA_ZIP, "rb") as f:
        zipped_code = f.read()
    lambda_client.create_function(
        FunctionName=function_name,
        Runtime="python3.8",
        Role="role",
        Handler=function_name + ".handler",
        Code=dict(ZipFile=zipped_code),
    )


def delete_lambda(function_name):
    lambda_client = get_lambda_client()
    lambda_client.delete_function(FunctionName=function_name)
    os.remove(LAMBDA_ZIP)


def create_bucket(bucket_name):
    s3_client = get_s3_client()
    s3_client.create_bucket(Bucket=bucket_name)


def delete_bucket(bucket_name):
    s3_client = get_s3_client()
    bucket_objects = s3_client.list_objects_v2(Bucket=bucket_name)["Contents"]
    [s3_client.delete_object(Bucket=bucket_name, Key=obj["Key"]) for obj in bucket_objects]
    s3_client.delete_bucket(Bucket=bucket_name)


def invoke_function(function_name, item):
    lambda_client = get_lambda_client()
    s3_client = get_s3_client()
    body = {"item": "meow"}
    response = lambda_client.invoke(
        FunctionName="s3_lambda", InvocationType="RequestResponse", Payload=json.dumps(body).encode("utf-8")
    )

    print(s3_client.list_objects_v2(Bucket="test-bucket"))
    final_response = response["Payload"].read().decode("utf-8")
    print(final_response)
    return json.loads(final_response)
