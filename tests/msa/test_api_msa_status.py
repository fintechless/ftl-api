"""
Tests for the STATUS microservice, part of the PLATFORM category
"""

import json
import urllib.parse
import uuid
from typing import Any
from typing import Dict

from flask.testing import FlaskClient
from werkzeug.test import TestResponse


# pylint: disable=R0903
class TestApiPlatformStatus:
    """
    Test class for testing the STATUS microservice
    """

    @staticmethod
    def test_api_platform_status_incoming_t_not_found_get(
        flask_test_client_msa_status: FlaskClient,
    ) -> None:
        """
        Test the GET /status endpoint with incoming=True
        Should return 404 status code
        """

        transaction_id: str = "55b8e027-bcb2-4e9f-b9ca-213777cd76b7"
        timestamp: str = urllib.parse.quote_plus("2022-02-04T13:59:25.664056+01:00")

        transaction_id_q: str = f"transaction_id={transaction_id}"
        timestamp_q: str = f"timestamp={timestamp}"

        response: TestResponse = flask_test_client_msa_status.get(
            f"/msa/status?{transaction_id_q}&{timestamp_q}&incoming=True&message_type=pacs.008.001.10"
        )

        assert response.status_code == 404

    @staticmethod
    def test_api_platform_status_incoming_f_not_found_get(
        flask_test_client_msa_status: FlaskClient,
    ) -> None:
        """
        Test the GET /status endpoint with incoming=False
        Should return 404 status code
        """

        transaction_id: str = "55b8e027-bcb2-4e9f-b9ca-213777cd76b7"
        timestamp: str = urllib.parse.quote_plus("2022-02-04T13:59:25.664056+01:00")

        transaction_id_q: str = f"transaction_id={transaction_id}"
        timestamp_q: str = f"timestamp={timestamp}"

        response: TestResponse = flask_test_client_msa_status.get(
            f"/msa/status?{transaction_id_q}&{timestamp_q}&incoming=False&message_type=pacs.008.001.10"
        )

        assert response.status_code == 404

    @staticmethod
    def test_api_platform_status_trailing_slash_get(
        flask_test_client_msa_status: FlaskClient,
    ) -> None:
        """
        Test the GET /status/ endpoint
        Should return 404 status code
        """

        response: TestResponse = flask_test_client_msa_status.get("/msa/status/")

        assert response.status_code == 404

    @staticmethod
    def test_api_platform_status_healty_get(
        flask_test_client_msa_status: FlaskClient,
    ) -> None:
        """
        Test the GET /status/_healthy endpoint
        Should return 200 status code
        """

        response: TestResponse = flask_test_client_msa_status.get(
            "/msa/status/_healthy"
        )

        data: Dict[str, Any] = json.loads(response.data)

        assert response.status_code == 200
        assert data.get("status") == "OK"
        assert data.get("request_id") == str(
            uuid.UUID(hex=data.get("request_id"), version=4)
        )

    @staticmethod
    def test_api_platform_status_healty_trailing_slash_get(
        flask_test_client_msa_status: FlaskClient,
    ) -> None:
        """
        Test the GET /status/_healthy/ endpoint
        Should return 404 status code
        """

        response: TestResponse = flask_test_client_msa_status.get(
            "/msa/status/_healthy/"
        )

        assert response.status_code == 404
