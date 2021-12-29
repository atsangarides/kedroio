import logging

logger = logging.getLogger(__name__)


def test_create_bucket(s3):
    s3.create_bucket(Bucket="somebucket")
    result = s3.list_buckets()
    assert len(result['Buckets']) == 1
    assert result['Buckets'][0]['Name'] == 'somebucket'
