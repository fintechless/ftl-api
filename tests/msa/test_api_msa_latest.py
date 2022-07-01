"""
Tests for the LATEST microservice, part of the PLATFORM category
"""


import json
import uuid
from typing import Any
from typing import Dict

from flask.testing import FlaskClient
from werkzeug.test import TestResponse


# pylint: disable=R0903
class TestApiPlatformLatest:
    """
    Test class for testing the LATEST microservice
    """

    @staticmethod
    def test_api_platform_latest_get(
        flask_test_client_msa_latest: FlaskClient,
    ) -> None:
        """
        Test the GET /latest endpoint
        Should return valid LATESTs
        """

        response: TestResponse = flask_test_client_msa_latest.get("/msa/latest")

        data: Dict[str, Any] = json.loads(response.data)

        assert response.status_code == 200
        assert data.get("status") == "OK"
        assert data.get("request_id") == str(
            uuid.UUID(hex=data.get("request_id"), version=4)
        )
        assert type(data.get("latest")) in (tuple, list)

    @staticmethod
    def test_api_platform_latest_trailing_slash_get(
        flask_test_client_msa_latest: FlaskClient,
    ) -> None:
        """
        Test the GET /latest endpoint
        Should return 404 status code
        """

        response: TestResponse = flask_test_client_msa_latest.get("/msa/latest/")

        assert response.status_code == 404

    @staticmethod
    def test_api_platform_latest_healty_get(
        flask_test_client_msa_latest: FlaskClient,
    ) -> None:
        """
        Test the GET /latest/_healthy endpoint
        Should return 200 status code
        """

        response: TestResponse = flask_test_client_msa_latest.get(
            "/msa/latest/_healthy"
        )

        data: Dict[str, Any] = json.loads(response.data)

        assert response.status_code == 200
        assert data.get("status") == "OK"
        assert data.get("request_id") == str(
            uuid.UUID(hex=data.get("request_id"), version=4)
        )

    @staticmethod
    def test_api_platform_latest_healty_trailing_slash_get(
        flask_test_client_msa_latest: FlaskClient,
    ) -> None:
        """
        Test the GET /latest/_healthy/ endpoint
        Should return 404 status code
        """

        response: TestResponse = flask_test_client_msa_latest.get(
            "/msa/latest/_healthy/"
        )

        assert response.status_code == 404
