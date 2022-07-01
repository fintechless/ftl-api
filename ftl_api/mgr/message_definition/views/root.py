"""
Flask view for the MESSAGE_DEFINITION blueprint
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
from ftl_python_lib.models_helper.message_definition import HelperMessageDefinition
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.message_definition.blueprints import BLUEPRINT_MESSAGE_DEFINITION


@BLUEPRINT_MESSAGE_DEFINITION.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /mgr/message/definition endpoint
    Retrieve message_definition for a given message_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing GET request for MESSAGE_DEFINITION message_definition"
    )
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    message_id: str = request.args.get("message_id")

    try:
        if message_id is None:
            LOGGER.logger.error("Missing message_id URL query")
            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "Server error",
                    "message": "Missing message_id URL query. Please provide a valid message_id value",
                },
                500,
            )

        message_definition_helper = HelperMessageDefinition(
            request_context=request_context, environ_context=environ_context
        )
        data = []

        message_definitions = message_definition_helper.get_by_message_id(message_id)

        for message_definition in message_definitions:
            data.append(
                {
                    "id": message_definition.reference_id,
                    "name": message_definition.name,
                    "type": message_definition.type,
                    "activated_at": message_definition.activated_at,
                    "message_id": message_definition.message_id,
                    "xsd_tag": message_definition.xsd_tag,
                    "annotation_name": message_definition.annotation_name,
                    "annotation_definition": message_definition.annotation_definition,
                    "parent_id": message_definition.parent_id,
                    "level": message_definition.level,
                    "is_leaf": message_definition.is_leaf,
                    "target_column": message_definition.target_column,
                    "target_type": message_definition.target_type,
                }
            )

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


@BLUEPRINT_MESSAGE_DEFINITION.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /mgr/message/definition endpoint
    Update a message_definition
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing PATCH request for MESSAGE_DEFINITION message_definition"
    )
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw message_definition
    message_definition_raw: Union[bytes, str] = request.data

    try:
        if len(message_definition_raw) == 0 or message_definition_raw is None:
            LOGGER.logger.error("Missing message_definition body")
            raise ExceptionInvalidRequest(
                message="Missing message_definition body",
                request_context=request_context,
            )

        if isinstance(request.data, bytes):
            body = bytes_to_str(src=request.data)
            body_json = json.loads(body)

            if body_json["owner_member_id"] is None:
                LOGGER.logger.error("Missing owner_member_id URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="""Missing owner_member_id URL query.
                        Please provide a valid owner_member_id value""",
                )

            if body_json["message_definition"]["id"] is None:
                LOGGER.logger.error("Missing message_definition URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="""Missing message_definition_id URL query.
                        Please provide a valid message_definition_id value""",
                )

            message_definition_helper = HelperMessageDefinition(
                request_context=request_context, environ_context=environ_context
            )
            message_definition_update = message_definition_helper.get_by_reference_id(
                body_json["message_definition"]["id"]
            )

            if isinstance(message_definition_update, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message_definition": 'This id doesn"t exist',
                    },
                    404,
                )

            _check_input_attributes(body_json, message_definition_update)

            response = message_definition_helper.update(
                message_definition_update=message_definition_update,
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
                        "activated_at": response.activated_at,
                        "message_id": response.message_id,
                        "xsd_tag": response.xsd_tag,
                        "annotation_name": response.annotation_name,
                        "annotation_definition": response.annotation_definition,
                        "parent_id": response.parent_id,
                        "level": response.level,
                        "is_leaf": response.is_leaf,
                        "target_column": response.target_column,
                        "target_type": response.target_type,
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


def _check_input_attributes(body_json, message_definition):
    if "target_column" in body_json["message_definition"]:
        message_definition.target_column = body_json["message_definition"][
            "target_column"
        ]

    if "target_type" in body_json["message_definition"]:
        message_definition.target_type = body_json["message_definition"]["target_type"]
