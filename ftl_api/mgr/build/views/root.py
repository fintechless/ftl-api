"""
Flask view for the BUILD blueprint
Path: /
"""

import json
import threading
from typing import Union

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
from ftl_python_lib.models_helper.codebuild import HelperCodeBuild
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.build.blueprints import BLUEPRINT_BUILD


def threaded(**kwargs) -> None:
    request_context: RequestContext = kwargs.get("request_context")
    environ_context: EnvironmentContext = kwargs.get("environ_context")
    id: str = kwargs.get("id")
    _build: bool = kwargs.get("build")
    build_helper = HelperCodeBuild(
        request_context=request_context, environ_context=environ_context, id=id
    )

    if _build:
        build_helper.deploy_repo_active()
        build_helper.deploy_repo_passive()
        build_helper.build_active()
        build_helper.build_passive()
    else:
        build_helper.deploy_all_active()
        build_helper.deploy_all_passive()


@BLUEPRINT_BUILD.route("", methods=["PATCH"])
def patch() -> Response:
    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for BUILD build")
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw message
    message_raw: Union[bytes, str] = request.data

    try:
        if len(message_raw) == 0 or message_raw is None:
            LOGGER.logger.error("Missing message body")
            raise ExceptionInvalidRequest(
                message="Missing message body", request_context=request_context
            )

        if isinstance(request.data, bytes):
            body = bytes_to_str(src=request.data)
            body_json = json.loads(body)

            if body_json["build"]["id"] is None:
                LOGGER.logger.error("Missing build URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing build_id URL query. Please provide a valid build_id value",
                )

            _build = True

            if "deploy" in body_json["build"]:
                _build = False

            threading.Thread(
                target=threaded,
                kwargs={
                    "request_context": request_context,
                    "environ_context": environ_context,
                    "id": body_json["build"]["id"],
                    "build": _build
                },
            ).start()

            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "OK",
                    "message": "Request was received",
                    "data": {},
                },
                200,
            )

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "Request was received",
                "data": {},
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
