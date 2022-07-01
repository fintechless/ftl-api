"""
Flask view for the MESSAGE_PARSER blueprint
Path: /
"""
import threading

from flask import Response
from flask import make_response
from flask import session
from ftl_python_lib.core.context.environment import EnvironmentContext
from ftl_python_lib.core.context.request import REQUEST_CONTEXT_SESSION
from ftl_python_lib.core.context.request import RequestContext
from ftl_python_lib.core.exceptions.client_invalid_request_exception import ExceptionInvalidRequest
from ftl_python_lib.core.exceptions.client_resource_not_found_exception import ExceptionResourceNotFound
from ftl_python_lib.core.log import LOGGER
from ftl_python_lib.models_helper.message_parser import HelperMessageParser

from ftl_api.mgr.message_parser.blueprints import BLUEPRINT_MESSAGE_PARSER


def threaded(**kwargs) -> None:
    request_context: RequestContext = kwargs.get("request_context")
    environ_context: EnvironmentContext = kwargs.get("environ_context")
    LOGGER.logger.debug("Proccessing for Microservice ISO 20022 Parser")
    message_helper = HelperMessageParser(
        request_context=request_context, environ_context=environ_context
    )
    message_helper.parser("cb308772-c49d-11ec-9d64-0242ac120002")


@BLUEPRINT_MESSAGE_PARSER.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /mgr/message/parser endpoint
    Update a message_parser
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for MESSAGE_PARSER message_parser")
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    try:
        LOGGER.logger.debug("Proccessing for Microservice ISO 20022 Parser")
        threading.Thread(
            target=threaded,
            kwargs={
                "request_context": request_context,
                "environ_context": environ_context,
            },
        ).start()
        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "Request was received",
                "data": {},
            },
            201,
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
