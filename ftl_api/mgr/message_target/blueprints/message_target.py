"""
Flask blueprint for MESSAGE_TARGET
"""

from typing import Any

from flask import Blueprint
from flask import Response
from flask import request
from flask import session
from flask.json import JSONEncoder
from ftl_python_lib.core.context.headers import HeadersContext
from ftl_python_lib.core.context.request import REQUEST_CONTEXT_SESSION
from ftl_python_lib.core.context.request import RequestContext
from ftl_python_lib.core.exceptions.client_invalid_request_exception import ExceptionInvalidRequest
from ftl_python_lib.core.exceptions.client_resource_not_found_exception import ExceptionResourceNotFound
from ftl_python_lib.core.exceptions.server_container_misconfigured_exception import ExceptionContainerMisconfigured
from ftl_python_lib.core.exceptions.server_unexpected_error_exception import ExceptionUnexpectedError
from ftl_python_lib.core.log import LOGGER


class CstmJsonEncoder(JSONEncoder):
    """
    Custom JSON Encoder for Flask blueprint
    """

    def default(self, o: Any) -> Any:
        if isinstance(o, (RequestContext, HeadersContext)):
            return o.to_dict()
        return super().default(o)


BLUEPRINT_MESSAGE_TARGET: Blueprint = Blueprint(
    "message_target",
    __name__,
    url_prefix="/mgr/message/target",
)

BLUEPRINT_MESSAGE_TARGET.json_encoder = CstmJsonEncoder


@BLUEPRINT_MESSAGE_TARGET.errorhandler(ExceptionInvalidRequest)
def exception_invalid_request(exc: ExceptionInvalidRequest) -> Response:
    """
    Handle ExceptionInvalidRequest
    """

    LOGGER.logger.debug("Handling exception ExceptionInvalidRequest")

    return exc.response()


@BLUEPRINT_MESSAGE_TARGET.errorhandler(ExceptionResourceNotFound)
def exception_resource_not_found(exc: ExceptionResourceNotFound) -> Response:
    """
    Handle ExceptionResourceNotFound
    """

    LOGGER.logger.debug("Handling exception ExceptionResourceNotFound")

    return exc.response()


@BLUEPRINT_MESSAGE_TARGET.errorhandler(ExceptionContainerMisconfigured)
def exception_container_misconfigured(exc: ExceptionContainerMisconfigured) -> Response:
    """
    Handle ExceptionContainerMisconfigured
    """

    LOGGER.logger.debug("Handling exception ExceptionContainerMisconfigured")

    return exc.response()


@BLUEPRINT_MESSAGE_TARGET.errorhandler(ExceptionUnexpectedError)
def exception_unexpected_error(exc: ExceptionUnexpectedError) -> Response:
    """
    Handle ExceptionUnexpectedError
    """

    LOGGER.logger.debug("Handling exception ExceptionUnexpectedError")

    return exc.response()


@BLUEPRINT_MESSAGE_TARGET.before_request
def push_contexts() -> None:
    """
    Generate the context before each HTTP request
    """

    LOGGER.logger.debug("Executing before_request hook for Flask")

    headers_context: HeadersContext = HeadersContext(headers=dict(request.headers))
    request_context: RequestContext = RequestContext(headers_context=headers_context)

    session[REQUEST_CONTEXT_SESSION] = request_context
