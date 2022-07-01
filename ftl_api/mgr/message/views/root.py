"""
Flask view for the MESSAGE blueprint
Path: /
"""

import base64
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
from ftl_python_lib.models.sql.message import ModelMessage
from ftl_python_lib.models_helper.message import HelperMessage
from ftl_python_lib.models_helper.message_category import HelperMessageCategory
from ftl_python_lib.models_helper.message_definition import HelperMessageDefinition
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.message.blueprints import BLUEPRINT_MESSAGE


@BLUEPRINT_MESSAGE.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /mgr/message endpoint
    Retrieve message for a given message_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for MESSAGE message")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    message_id: str = request.args.get("message_id")

    try:
        message_helper = HelperMessage(
            request_context=request_context, environ_context=environ_context
        )
        data = NoneType
        if message_id is None:
            message_response = []
            message_list = message_helper.get_all()
            for message in message_list:
                message_response.append(
                    {
                        "id": message.reference_id,
                        "unique_key": message.unique_key,
                        "active": message.active,
                        "description": message.description,
                        "category_id": message.category_id,
                        "org": message.org,
                        "url": message.url,
                    }
                )
            data = message_response
        else:
            message = message_helper.get_by_reference_id(message_id)

            if isinstance(message, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            data = {
                "id": message.reference_id,
                "unique_key": message.unique_key,
                "active": message.active,
                "description": message.description,
                "org": message.org,
                "url": message.url,
                "category_id": message.category_id,
                "unique_type": message.unique_type,
                "version_major": message.version_major,
                "version_minor": message.version_minor,
                "version_patch": message.version_patch,
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


@BLUEPRINT_MESSAGE.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /mgr/message endpoint
    Update a message
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for MESSAGE message")
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

            if body_json["owner_member_id"] is None:
                LOGGER.logger.error("Missing owner_member_id URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
                )

            if body_json["message"]["id"] is None:
                LOGGER.logger.error("Missing message URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing message_id URL query. Please provide a valid message_id value",
                )

            message_helper = HelperMessage(
                request_context=request_context, environ_context=environ_context
            )
            message_update = message_helper.get_reference_id(body_json["message"]["id"])

            if isinstance(message_update, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            _check_input_update_attributes(body_json, message_update)

            message_bytes = None
            if "content" in body_json["message"]:
                message_bytes = base64.b64decode(body_json["message"]["content"])

            response = message_helper.update(
                message_update=message_update,
                owner_member_id=body_json["owner_member_id"],
                content=message_bytes,
            )

            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "OK",
                    "message": "Request was received",
                    "data": {
                        "id": response.reference_id,
                        "child_id": response.child_id,
                        "active": response.active,
                        "unique_key": response.unique_key,
                        "description": response.description,
                        "org": response.org,
                        "url": response.url,
                        "category_id": response.category_id,
                        "unique_type": response.unique_type,
                        "version_major": response.version_major,
                        "version_minor": response.version_minor,
                        "version_patch": response.version_patch,
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


def _check_input_attributes(body_json, message):
    _check_input_update_attributes(body_json, message)

    if "category_id" in body_json["message"]:
        message.category_id = body_json["message"]["category_id"]

    if "version_major" in body_json["message"]:
        message.version_major = body_json["message"]["version_major"]

    if "version_minor" in body_json["message"]:
        message.version_minor = body_json["message"]["version_minor"]

    if "version_patch" in body_json["message"]:
        message.version_patch = body_json["message"]["version_patch"]

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    category_helper = HelperMessageCategory(
        request_context=request_context, environ_context=environ_context
    )
    category = category_helper.get_by_reference_id(message.category_id)
    message.unique_type = category.name
    message.unique_key = f"{message.unique_type}.{message.version_major}"


def _check_input_update_attributes(body_json, message):
    if "active" in body_json["message"]:
        message.active = body_json["message"]["active"]

    if message.active is None:
        message.active = False

    if "description" in body_json["message"]:
        message.description = body_json["message"]["description"]


@BLUEPRINT_MESSAGE.route("", methods=["POST"])
def post() -> Response:
    """
    Process PATCH request for the /message endpoint
    Create new message
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for MESSAGE message")
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

            _check_params(request_context, body_json)

            message_new: ModelMessage = ModelMessage()

            _check_input_attributes(body_json, message_new)

            message_helper = HelperMessage(
                request_context=request_context, environ_context=environ_context
            )
            message_exist = message_helper.get_by_key(
                unique_type=message_new.unique_type,
                version_major=message_new.version_major,
                version_minor=message_new.version_minor,
                version_patch=message_new.version_patch,
            )

            if message_exist is not None:
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "OK",
                        "message": "This message exists.",
                        "data": {},
                    },
                    400,
                )
            message_bytes = base64.b64decode(body_json["message"]["content"])
            response = message_helper.create(
                message_new=message_new,
                owner_member_id=body_json["owner_member_id"],
                content=message_bytes,
            )

            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "OK",
                    "message": "Request was received",
                    "data": {
                        "id": response.reference_id,
                        "unique_key": response.unique_key,
                        "active": response.active,
                        "description": response.description,
                        "category_id": response.category_id,
                        "org": response.org,
                        "url": response.url,
                        "unique_type": response.unique_type,
                        "version_major": response.version_major,
                        "version_minor": response.version_minor,
                        "version_patch": response.version_patch,
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


def _check_params(request_context, body_json):
    if body_json["owner_member_id"] is None:
        LOGGER.logger.error("Missing owner_member_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
        )

    if body_json["message"] is None:
        LOGGER.logger.error("Missing message URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing message URL query. Please provide a valid message value",
        )

    if body_json["message"]["category_id"] is None:
        LOGGER.logger.error("Missing category_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing category_id URL query. Please provide a valid category_id value",
        )

    if body_json["message"]["version_major"] is None:
        LOGGER.logger.error("Missing version_major URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing version_major URL query. Please provide a valid version_major value",
        )

    if body_json["message"]["version_patch"] is None:
        LOGGER.logger.error("Missing version_patch URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing version_patch URL query. Please provide a valid version_patch value",
        )

    if body_json["message"]["content"] is None:
        LOGGER.logger.error("Missing content URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing content URL query. Please provide a valid content value",
        )


@BLUEPRINT_MESSAGE.route("", methods=["DELETE"])
def delete() -> Response:
    """
    Process GET request for the /message endpoint
    Delete message for a given message_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for MESSAGE message")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    if request.args.get("message_id") is None:
        LOGGER.logger.error("Missing message_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing message_id URL query. Please provide a valid message_id value",
        )

    message_id: str = request.args.get("message_id")

    if request.args.get("owner_member_id") is None:
        LOGGER.logger.error("Missing owner_member_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
        )

    owner_member_id: str = request.args.get("owner_member_id")

    try:
        message_helper = HelperMessage(
            request_context=request_context, environ_context=environ_context
        )
        message_helper.delete_by_id(owner_member_id, message_id)

        message_definition_helper = HelperMessageDefinition(
            request_context=request_context, environ_context=environ_context
        )
        message_definition_helper.delete_by_message_id(owner_member_id, message_id)

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "Message was deleted",
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
