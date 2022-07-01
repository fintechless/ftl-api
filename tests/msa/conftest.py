"""
Pytest configuration file
Used for defining fixtures
"""

import os

import mock
import pytest
from flask.testing import FlaskClient

import ftl_api.msa.latest.run
import ftl_api.msa.ping.run
import ftl_api.msa.status.run
import ftl_api.msa.uuid.run


@pytest.fixture(autouse=True)
def mock_base_environ() -> str:
    """
    Add relevant environment variables
    """

    environ: dict = {
        "AWS_ACCESS_KEY_ID": "dummyaccess",
        "AWS_SECRET_ACCESS_KEY": "dummysecret",
        "AWS_DEFAULT_REGION": "us-east-1",
        "AWS_ACCOUNT_ID": "123456789012",
        "KAFKA_BROKER": "localhost:9092",
        "KAFKA_MESSAGE_INBOX_TARGET": "topic-msg-in-pacs-008",
        "KAFKA_MESSAGE_OUTBOX_TARGET": "topic-msg-out-pacs-008",
        "FTL_ENVIRONMENT": "default",
        "FTL_CLOUD_REGION_PRIMARY": "us-east-1",
        "FTL_CLOUD_PROVIDER_API_ENDPOINT_URL": "http://localhost:4566",
        "FTL_MSA_UUID_TTL": "5",
        "FTL_RUNTIME_BUCKET": "ftl-api-runtime-default-us-east-1-123456789012",
    }

    with mock.patch.dict(os.environ, environ):
        yield


@pytest.fixture
def flask_test_client_msa_ping() -> FlaskClient:
    """
    Create test client of the FLASK application for MSA UUID
    """
    return ftl_api.msa.ping.run.create_app().test_client()


@pytest.fixture
def flask_test_client_msa_uuid() -> FlaskClient:
    """
    Create test client of the FLASK application for MSA UUID
    """
    return ftl_api.msa.uuid.run.create_app().test_client()


@pytest.fixture
def flask_test_client_msa_latest() -> FlaskClient:
    """
    Create test client of the FLASK application for MSA LATEST
    """
    return ftl_api.msa.latest.run.create_app().test_client()


@pytest.fixture
def flask_test_client_msa_status() -> FlaskClient:
    """
    Create test client of the FLASK application for MSA STATUS
    """
    return ftl_api.msa.status.run.create_app().test_client()
