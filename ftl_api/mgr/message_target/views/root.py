"""
Flask view for the MESSAGE_TARGET blueprint
Path: /
"""

import json
from types import NoneType
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
from ftl_python_lib.models.sql.message_target import ModelMessageTarget
from ftl_python_lib.models_helper.message_target import HelperMessageTarget
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.message_target.blueprints import BLUEPRINT_MESSAGE_TARGET


@BLUEPRINT_MESSAGE_TARGET.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /mgr/message/target endpoint
    Retrieve message_target for a given message_target_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for MESSAGE_TARGET message_target")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    message_target_id: str = request.args.get("message_target_id")

    try:
        message_target_helper = HelperMessageTarget(
            request_context=request_context, environ_context=environ_context
        )
        data = NoneType
        if message_target_id is None:
            data = []
            for message_target in message_target_helper.get_all():
                data.append(
                    {
                        "id": message_target.reference_id,
                        "name": message_target.name,
                        "type": message_target.type,
                    }
                )
        else:
            message_target = message_target_helper.get_by_reference_id(
                message_target_id
            )

            if isinstance(message_target, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            data = {
                "id": message_target.reference_id,
                "name": message_target.name,
                "type": message_target.type,
            }

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


@BLUEPRINT_MESSAGE_TARGET.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /mgr/message/target endpoint
    Update a message_target
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for MESSAGE_TARGET message_target")
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw message_target
    message_target_raw: Union[bytes, str] = request.data

    try:
        if len(message_target_raw) == 0 or message_target_raw is None:
            LOGGER.logger.error("Missing message_target body")
            raise ExceptionInvalidRequest(
                message="Missing message_target body",
                request_context=request_context,
            )

        if isinstance(request.data, bytes):
            body = bytes_to_str(src=request.data)
            body_json = json.loads(body)

            if body_json["owner_member_id"] is None:
                LOGGER.logger.error("Missing owner_member_id URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
                )

            if body_json["message_target"]["id"] is None:
                LOGGER.logger.error("Missing message_target URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="""Missing message_target_id URL query.
                        Please provide a valid message_target_id value""",
                )

            message_target_helper = HelperMessageTarget(
                request_context=request_context, environ_context=environ_context
            )
            message_target_update = message_target_helper.get_by_reference_id(
                body_json["message_target"]["id"]
            )

            if isinstance(message_target_update, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            _check_input_attributes(body_json, message_target_update)

            response = message_target_helper.update(
                message_target_update=message_target_update,
                owner_member_id=body_json["owner_member_id"],
            )

            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "OK",
                    "message": "Request was received",
                    "data": {
                        "id": response.reference_id,
                        "child_id": response.child_id,
                        "name": response.name,
                        "type": response.type,
                    },
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


def _check_input_attributes(body_json, message_target):
    if "name" in body_json["message_target"]:
        message_target.name = body_json["message_target"]["name"]

    if "type" in body_json["message_target"]:
        message_target.type = body_json["message_target"]["type"]


@BLUEPRINT_MESSAGE_TARGET.route("", methods=["POST"])
def post() -> Response:
    """
    Process PATCH request for the /message_target endpoint
    Create new message_target
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for MESSAGE_TARGET message_target")
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw message_target
    message_target_raw: Union[bytes, str] = request.data

    try:
        if len(message_target_raw) == 0 or message_target_raw is None:
            LOGGER.logger.error("Missing message_target body")
            raise ExceptionInvalidRequest(
                message="Missing message_target body",
                request_context=request_context,
            )

        if isinstance(request.data, bytes):
            body = bytes_to_str(src=request.data)
            body_json = json.loads(body)

            if body_json["owner_member_id"] is None:
                LOGGER.logger.error("Missing owner_member_id URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
                )

            if body_json["message_target"] is None:
                LOGGER.logger.error("Missing message_target URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
                )

            message_target_new: ModelMessageTarget = ModelMessageTarget(
                name=body_json["message_target"]["name"]
            )

            _check_input_attributes(body_json, message_target_new)

            message_target_helper = HelperMessageTarget(
                request_context=request_context, environ_context=environ_context
            )

            message_target_exist = message_target_helper.get_by_name(
                message_target_new.name
            )
            if message_target_exist is not None:
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "OK",
                        "message": "This message_target exists.",
                        "data": {},
                    },
                    400,
                )

            response = message_target_helper.create(
                message_target_new=message_target_new,
                owner_member_id=body_json["owner_member_id"],
            )

            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "OK",
                    "message": "Request was received",
                    "data": {
                        "id": response.reference_id,
                        "name": response.name,
                        "type": response.type,
                    },
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


@BLUEPRINT_MESSAGE_TARGET.route("", methods=["DELETE"])
def delete() -> Response:
    """
    Process GET request for the /message_target endpoint
    Delete message_target for a given message_target_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for MESSAGE_TARGET message_target")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    if request.args.get("message_target_id") is None:
        LOGGER.logger.error("Missing message_target_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing message_target_id URL query. Please provide a valid message_target_id value",
        )

    message_target_id: str = request.args.get("message_target_id")

    if request.args.get("owner_member_id") is None:
        LOGGER.logger.error("Missing owner_member_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
        )

    owner_member_id: str = request.args.get("owner_member_id")

    try:
        message_target_helper = HelperMessageTarget(
            request_context=request_context, environ_context=environ_context
        )
        message_target_exist = message_target_helper.get_by_reference_id(
            message_target_id
        )

        if isinstance(message_target_exist, NoneType):
            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "Not found",
                    "message": 'This id doesn"t exist',
                },
                404,
            )

        message_target_helper.delete_by_id(owner_member_id, message_target_id)

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "MessageTarget was deleted",
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
