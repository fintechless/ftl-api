"""
Flask view for the DASHBOARD blueprint
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
from ftl_python_lib.core.exceptions.client_resource_not_found_exception import ExceptionResourceNotFound
from ftl_python_lib.core.log import LOGGER
from ftl_python_lib.models_helper.dashboard import HelperDashboard

from ftl_api.mgr.dashboard.blueprints import BLUEPRINT_DASHBOARD


@BLUEPRINT_DASHBOARD.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /mgr/message/target endpoint
    Retrieve dashboard for a given dashboard_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for DASHBOARD dashboard")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    from_date: str = request.args.get("from_date")
    to_date: str = request.args.get("to_date")

    try:
        dashboard_helper = HelperDashboard(
            request_context=request_context, environ_context=environ_context
        )
        data = {}

        if from_date is None and to_date is None:
            data = dashboard_helper.get_static_info()
        else:
            data = dashboard_helper.get_dynamic_info(from_date, to_date)

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "Request was received",
                "data": data,
            },
            200,
        )
    except (ExceptionInvalidRequest, ExceptionResourceNotFound) as error:
        LOGGER.logger.error(error)
        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "Server error",
                "message": f"Unexpected server error: {str(error)}",
            },
            500,
        )
    except Exception as err:
        LOGGER.logger.error(err)
        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "Server error",
                "message": f"Unexpected server error: {str(err)}",
            },
            500,
        )
