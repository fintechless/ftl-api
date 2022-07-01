"""
Flask view for the LATEST blueprint
Path: /
"""

from flask import Response
from flask import make_response
from flask import session
from ftl_python_lib.core.context.environment import EnvironmentContext
from ftl_python_lib.core.context.request import REQUEST_CONTEXT_SESSION
from ftl_python_lib.core.context.request import RequestContext
from ftl_python_lib.core.log import LOGGER
from ftl_python_lib.models.transaction import ModelTransaction
from ftl_python_lib.typings.models.transaction import TypeTransaction

from ftl_api.msa.latest.blueprints import BLUEPRINT_LATEST


@BLUEPRINT_LATEST.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /latest endpoint
    Retrived latest transactions
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.debug("Proccessing GET request for LATEST microservice")
    LOGGER.logger.debug(f"Request ID is {request_context.request_id}")
    LOGGER.logger.debug(
        f"Request timestamp is {request_context.requested_at_isoformat}"
    )

    transaction_model: ModelTransaction = ModelTransaction(
        request_context=request_context, environ_context=environ_context
    )

    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    latest: list[TypeTransaction] = transaction_model.latest()

    return make_response(
        {
            "request_id": request_context.request_id,
            "latest": latest,
            "status": "OK",
        },
        200,
    )
