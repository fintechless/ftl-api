"""
Tests for the UUID microservice, part of the PLATFORM category
"""


import json
import uuid
from typing import Any
from typing import Dict

from flask.testing import FlaskClient
from werkzeug.test import TestResponse


# pylint: disable=R0903
class TestApiPlatformUuid:
    """
    Test class for testing the UUID microservice
    """

    @staticmethod
    def test_api_platform_uuid_post(flask_test_client_msa_uuid: FlaskClient) -> None:
        """
        Test the POST /uuid endpoint
        Should return valid UUIDs
        """

        response: TestResponse = flask_test_client_msa_uuid.post("/msa/uuid")

        data: Dict[str, Any] = json.loads(response.data)

        assert response.status_code == 200
        assert data.get("status") == "OK"
        assert data.get("request_id") == str(
            uuid.UUID(hex=data.get("request_id"), version=4)
        )
        assert data.get("transaction_id") == str(
            uuid.UUID(hex=data.get("transaction_id"), version=4)
        )

    @staticmethod
    def test_api_platform_uuid_trailing_slash_post(
        flask_test_client_msa_uuid: FlaskClient,
    ) -> None:
        """
        Test the POST /uuid/ endpoint
        Should return 404 status code
        """

        response: TestResponse = flask_test_client_msa_uuid.post("/msa/uuid/")

        assert response.status_code == 404

    @staticmethod
    def test_api_platform_uuid_healty_get(
        flask_test_client_msa_uuid: FlaskClient,
    ) -> None:
        """
        Test the GET /uuid/_healthy endpoint
        Should return 200 status code
        """

        response: TestResponse = flask_test_client_msa_uuid.get("/msa/uuid/_healthy")

        data: Dict[str, Any] = json.loads(response.data)

        assert response.status_code == 200
        assert data.get("status") == "OK"
        assert data.get("request_id") == str(
            uuid.UUID(hex=data.get("request_id"), version=4)
        )

    @staticmethod
    def test_api_platform_uuid_healty_trailing_slash_get(
        flask_test_client_msa_uuid: FlaskClient,
    ) -> None:
        """
        Test the GET /uuid/_healthy/ endpoint
        Should return 404 status code
        """

        response: TestResponse = flask_test_client_msa_uuid.get("/msa/uuid/_healthy/")

        assert response.status_code == 404
