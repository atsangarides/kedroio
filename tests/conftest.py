import os

import pytest
import boto3
import requests
# from sqlalchemy import *
# from sqlalchemy.engine import create_engine


@pytest.fixture(scope='function')
def moto_endpoint():
    return "http://127.0.0.1:5000"


@pytest.fixture(scope='function')
def s3(moto_endpoint):
    yield boto3.client('s3', endpoint_url=moto_endpoint)
    teardown_moto(moto_endpoint)


@pytest.fixture(scope='function')
def athena(moto_endpoint):
    yield boto3.client('athena', endpoint_url=moto_endpoint)
    # teardown_moto(moto_endpoint)


# @pytest.fixture(scope='function')
# def hive():
#     yield create_engine("hive://localhost:10000")
#
#
# @pytest.fixture(scope='function')
# def presto():
#     yield create_engine("presto://localhost:8080/hive")
#
#
# @pytest.fixture(scope="function")
# def athena_table(s3, athena, hive):
#     # create s3 bucket and upload csv
#     s3.create_bucket(
#         Bucket="mothena", CreateBucketConfiguration={"LocationConstraint": "eu-west-2"}
#     )
#     with open("tests/data/simple_data.csv", "rb") as f:
#         s3.put_object(Bucket="mothena", Key="tests/simple_data.csv", Body=f.read())
#     # create athena table
#     ddl = (
#         """
#         CREATE EXTERNAL TABLE ny_data(
#             col1 string,
#             col2 string
#         )
#         ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
#         LOCATION 's3a://mothena/tests
#         '"""
#     )
#     hive.execute(QueryString=ddl)
#     hive.execute("MSCK REPAIR TABLE ny_data")




def teardown_moto(moto_endpoint):
    url = os.path.join(moto_endpoint, "moto-api/reset")
    response = requests.post(url)
    assert response.status_code == 200


