"""
Flask view for the STATUS blueprint
Path: /
"""

import urllib.parse

from flask import Response
from flask import make_response
from flask import request
from flask import session
from ftl_python_lib.core.context.environment import EnvironmentContext
from ftl_python_lib.core.context.request import REQUEST_CONTEXT_SESSION
from ftl_python_lib.core.context.request import RequestContext
from ftl_python_lib.core.exceptions.client_invalid_request_exception import ExceptionInvalidRequest
from ftl_python_lib.core.exceptions.client_resource_not_found_exception import ExceptionResourceNotFound
from ftl_python_lib.core.log import LOGGER
from ftl_python_lib.core.providers.aws.s3 import ProviderS3
from ftl_python_lib.models.transaction import ModelTransaction
from ftl_python_lib.utils.timedate import DateTime
from ftl_python_lib.utils.timedate import UtilsDatetime
from ftl_python_lib.utils.to_bool import UtilsConversionsToBool
from ftl_python_lib.utils.xml.storage import storage_key

from ftl_api.msa.status.blueprints import BLUEPRINT_STATUS


@BLUEPRINT_STATUS.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /status endpoint
    Retrieve status for a given transaction_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for STATUS microservice")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    # Transaction
    transaction_id: str = request.args.get("transaction_id")
    message_type: str = request.args.get("message_type")
    # Timestamp
    _timestamp: str = request.args.get("timestamp")
    timestamp: DateTime = None
    # Incoming
    _incoming: str = request.args.get("incoming")
    incoming: bool = False

    if transaction_id is None:
        LOGGER.logger.error("Missing transaction_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing transaction_id URL query. Please provide a valid transaction_id value",
        )
    if message_type is None:
        LOGGER.logger.error("Missing message_type URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing message_type URL query. Please provide a valid message_type value",
        )

    if _timestamp is None:
        LOGGER.logger.error("Missing timestamp URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing timestamp URL query. Please provide a valid timestamp value",
        )
    try:
        timestamp = UtilsDatetime(from_source=urllib.parse.unquote(_timestamp)).now
    except Exception as exc:
        LOGGER.logger.error("Could not convert timestamp to datetime.datetime")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Received an invalid timestamp value. Please provide a valid timestamp value",
        ) from exc

    if _incoming is not None:
        try:
            incoming = UtilsConversionsToBool.str_to_bool(src=_incoming)
        except Exception as exc:
            LOGGER.logger.error("Could not convert incoming to bool")
            raise ExceptionInvalidRequest(
                request_context=request_context,
                message="Received an invalid incoming value. Please provide a valid incoming value",
            ) from exc

    provider_s3: ProviderS3 = ProviderS3(
        request_context=request_context, environ_context=environ_context
    )
    transaction_model: ModelTransaction = ModelTransaction(
        request_context=request_context, environ_context=environ_context
    )

    if transaction_model.exists() is False:
        LOGGER.logger.error("Could not find such transaction")
        raise ExceptionResourceNotFound(
            request_context=request_context,
            message="Could not find such transaction",
        )

    body: str = provider_s3.get_object_body(
        bucket=environ_context.runtime_bucket,
        key=storage_key(
            transaction_id=request_context.transaction_id,
            incoming=incoming,
            message_version=message_type,
            requested_at=timestamp,
        ),
    )

    transaction_model.retrieve()
    transaction_model.retrieved()

    return make_response(
        body,
        200,
    )
