"""
Flask view for the PROVIDER_CATEGORY blueprint
Path: /
"""

from flask import Response
from flask import make_response
from flask import session
from ftl_python_lib.core.context.request import REQUEST_CONTEXT_SESSION
from ftl_python_lib.core.context.request import RequestContext
from ftl_python_lib.core.log import LOGGER

from ftl_api.mgr.provider_category.blueprints import BLUEPRINT_PROVIDER_CATEGORY


@BLUEPRINT_PROVIDER_CATEGORY.route("_healthy", methods=["GET"])
def healthy() -> Response:
    """
    Process GET request for the /mgr/provider/category/_healthy endpoint
    Dummy GET for ELB healthcheck
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)

    LOGGER.logger.debug(
        "Proccessing GET request for PROVIDER_CATEGORY provider_category"
    )
    LOGGER.logger.debug(f"Request ID is {request_context.request_id}")
    LOGGER.logger.debug(
        f"Request timestamp is {request_context.requested_at_isoformat}"
    )

    return make_response(
        {
            "request_id": request_context.request_id,
            "status": "OK",
            "message": "Healthy",
        },
        200,
    )
