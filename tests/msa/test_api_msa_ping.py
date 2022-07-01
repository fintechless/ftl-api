"""
Tests for the PING microservice, part of the PLATFORM category
"""


import json
import uuid
from typing import Any
from typing import Dict

from flask.testing import FlaskClient
from werkzeug.test import TestResponse


# pylint: disable=R0903
class TestApiPlatformPing:
    """
    Test class for testing the PING microservice
    """

    @staticmethod
    def test_api_platform_ping_get(flask_test_client_msa_ping: FlaskClient) -> None:
        """
        Test the GET /ping endpoint
        Should return valid UUIDs
        """

        response: TestResponse = flask_test_client_msa_ping.get("/msa/ping")

        data: Dict[str, Any] = json.loads(response.data)

        assert response.status_code == 200
        assert data.get("status") == "OK"
        assert data.get("request_id") == str(
            uuid.UUID(hex=data.get("request_id"), version=4)
        )

    @staticmethod
    def test_api_platform_ping_traling_slash_get(
        flask_test_client_msa_ping: FlaskClient,
    ) -> None:
        """
        Test the GET /ping/ endpoint
        Should return 404 status code
        """

        response: TestResponse = flask_test_client_msa_ping.get("/msa/ping/")

        assert response.status_code == 404

    @staticmethod
    def test_api_platform_ping_healty_get(
        flask_test_client_msa_ping: FlaskClient,
    ) -> None:
        """
        Test the GET /ping/_healthy endpoint
        Should return 200 status code
        """

        response: TestResponse = flask_test_client_msa_ping.get("/msa/ping/_healthy")

        data: Dict[str, Any] = json.loads(response.data)

        assert response.status_code == 200
        assert data.get("status") == "OK"
        assert data.get("request_id") == str(
            uuid.UUID(hex=data.get("request_id"), version=4)
        )

    @staticmethod
    def test_api_platform_ping_healty_trailing_slash_get(
        flask_test_client_msa_ping: FlaskClient,
    ) -> None:
        """
        Test the GET /ping/_healthy/ endpoint
        Should return 404 status code
        """

        response: TestResponse = flask_test_client_msa_ping.get("/msa/ping/_healthy/")

        assert response.status_code == 404
