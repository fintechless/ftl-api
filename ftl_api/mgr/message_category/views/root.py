"""
Flask view for the MESSAGE_CATEGORY blueprint
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
from ftl_python_lib.models.sql.message_category import ModelMessageCategory
from ftl_python_lib.models_helper.message_category import HelperMessageCategory
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.message_category.blueprints import BLUEPRINT_MESSAGE_CATEGORY


@BLUEPRINT_MESSAGE_CATEGORY.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /mgr/message/category endpoint
    Retrieve message_category for a given message_category_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for MESSAGE_CATEGORY message_category")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    message_category_id: str = request.args.get("message_category_id")

    try:
        message_category_helper = HelperMessageCategory(
            request_context=request_context, environ_context=environ_context
        )
        data = NoneType
        if message_category_id is None:
            data = []
            for message_category in message_category_helper.get_all():
                data.append(
                    {
                        "id": message_category.reference_id,
                        "name": message_category.name,
                        "description": message_category.description,
                    }
                )
        else:
            message_category = message_category_helper.get_by_reference_id(
                message_category_id
            )

            if isinstance(message_category, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            data = {
                "id": message_category.reference_id,
                "name": message_category.name,
                "description": message_category.description,
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


@BLUEPRINT_MESSAGE_CATEGORY.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /mgr/message/category endpoint
    Update a message_category
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing PATCH request for MESSAGE_CATEGORY message_category"
    )
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw message_category
    message_category_raw: Union[bytes, str] = request.data

    try:
        if len(message_category_raw) == 0 or message_category_raw is None:
            LOGGER.logger.error("Missing message_category body")
            raise ExceptionInvalidRequest(
                message="Missing message_category body",
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

            if body_json["message_category"]["id"] is None:
                LOGGER.logger.error("Missing message_category URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="""Missing message_category_id URL query.
                        Please provide a valid message_category_id value""",
                )

            message_category_helper = HelperMessageCategory(
                request_context=request_context, environ_context=environ_context
            )
            message_category_update = message_category_helper.get_by_reference_id(
                body_json["message_category"]["id"]
            )

            if isinstance(message_category_update, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            _check_input_attributes(body_json, message_category_update)

            response = message_category_helper.update(
                message_category_update=message_category_update,
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
                        "description": response.description,
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


def _check_input_attributes(body_json, message_category):
    if "name" in body_json["message_category"]:
        message_category.name = body_json["message_category"]["name"]

    if "description" in body_json["message_category"]:
        message_category.description = body_json["message_category"]["description"]


@BLUEPRINT_MESSAGE_CATEGORY.route("", methods=["POST"])
def post() -> Response:
    """
    Process PATCH request for the /message_category endpoint
    Create new message_category
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing PATCH request for MESSAGE_CATEGORY message_category"
    )
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw message_category
    message_category_raw: Union[bytes, str] = request.data

    try:
        if len(message_category_raw) == 0 or message_category_raw is None:
            LOGGER.logger.error("Missing message_category body")
            raise ExceptionInvalidRequest(
                message="Missing message_category body",
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

            if body_json["message_category"] is None:
                LOGGER.logger.error("Missing message_category URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
                )

            message_category_new: ModelMessageCategory = ModelMessageCategory(
                name=body_json["message_category"]["name"]
            )

            _check_input_attributes(body_json, message_category_new)

            message_category_helper = HelperMessageCategory(
                request_context=request_context, environ_context=environ_context
            )

            message_category_exist = message_category_helper.get_by_name(
                message_category_new.name
            )
            if message_category_exist is not None:
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "OK",
                        "message": "This message_category exists.",
                        "data": {},
                    },
                    400,
                )

            response = message_category_helper.create(
                message_category_new=message_category_new,
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
                        "description": response.description,
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


@BLUEPRINT_MESSAGE_CATEGORY.route("", methods=["DELETE"])
def delete() -> Response:
    """
    Process GET request for the /message_category endpoint
    Delete message_category for a given message_category_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for MESSAGE_CATEGORY message_category")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    if request.args.get("message_category_id") is None:
        LOGGER.logger.error("Missing message_category_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing message_category_id URL query. Please provide a valid message_category_id value",
        )

    message_category_id: str = request.args.get("message_category_id")

    if request.args.get("owner_member_id") is None:
        LOGGER.logger.error("Missing owner_member_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
        )

    owner_member_id: str = request.args.get("owner_member_id")

    try:
        message_category_helper = HelperMessageCategory(
            request_context=request_context, environ_context=environ_context
        )
        message_category_exist = message_category_helper.get_by_reference_id(
            message_category_id
        )

        if isinstance(message_category_exist, NoneType):
            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "Not found",
                    "message": 'This id doesn"t exist',
                },
                404,
            )

        message_category_helper.delete_by_id(owner_member_id, message_category_id)

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "MessageCategory was deleted",
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
