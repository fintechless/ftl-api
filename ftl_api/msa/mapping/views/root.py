"""
Flask view for the MAPPING blueprint
Path: /
"""

from flask import Response
from flask import make_response
from flask import request
from flask import session
from ftl_python_lib.core.context.environment import EnvironmentContext
from ftl_python_lib.core.context.request import REQUEST_CONTEXT_SESSION
from ftl_python_lib.core.context.request import RequestContext
from ftl_python_lib.core.exceptions.client_invalid_request_exception import ExceptionInvalidRequest
from ftl_python_lib.core.log import LOGGER
from ftl_python_lib.models_helper.mapping import HelperMapping

from ftl_api.msa.mapping.blueprints import BLUEPRINT_MAPPING


@BLUEPRINT_MAPPING.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /mapping endpoint
    Retrived mapping transactions
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.debug(
        "\n".join(
            [
                "Proccessing POST request for MAPPING microservice",
                f"Request ID is {request_context.request_id}",
                f"Transaction ID is {request_context.transaction_id}",
                f"Request timestamp is {request_context.requested_at_datetime}",
            ]
        )
    )

    source: str = request.args.get("source")
    source_type: str = request.args.get("source_type")
    content_type: str = request.args.get("content_type")
    message_type: str = request.args.get("message_type")
    target: str = request.args.get("target")

    if (
        source is None
        and source_type is None
        and content_type is None
        and message_type is None
        and target is None
    ):
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="At least one query parameter must be included",
        )

    helper_mapping: HelperMapping = HelperMapping(
        request_context=request_context, environ_context=environ_context
    )

    res = helper_mapping.get_all(
        filters={
            "source": source,
            "source_type": source_type,
            "content_type": content_type,
            "message_type": message_type,
            "target": target,
        }
    )

    return make_response(
        {
            "request_id": request_context.request_id,
            "status": "OK",
            "data": [dict(it) for it in res],
        },
        200,
    )
