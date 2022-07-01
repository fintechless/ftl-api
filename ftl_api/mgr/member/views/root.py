"""
Flask view for the MEMBER blueprint
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
from ftl_python_lib.models_helper.member import HelperMember
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.member.blueprints import BLUEPRINT_MEMBER


@BLUEPRINT_MEMBER.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /member endpoint
    Retrieve member for a given member_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for MEMBER member")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    member_id: str = request.args.get("member_id")
    auth_id: str = request.args.get("auth_id")
    auth_email: str = request.args.get("auth_email")

    try:
        member_helper = HelperMember(
            request_context=request_context, environ_context=environ_context
        )
        member = NoneType
        if member_id is None:
            member = member_helper.get_by_auth_id(auth_id, auth_email)
        else:
            member = member_helper.get_reference_id(member_id)
            if isinstance(member, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "Request was received",
                "data": {
                    "id": member.reference_id,
                    "auth_id": member.auth_id,
                    "email": member.email,
                    "first_name": member.first_name,
                    "last_name": member.last_name,
                    "avatar": member.avatar,
                    "role": member.role,
                    "invite": member.invite,
                },
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


@BLUEPRINT_MEMBER.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /member endpoint
    Update a member
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for MEMBER member")
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

            if body_json["member"]["id"] is None:
                LOGGER.logger.error("Missing member URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing member_id URL query. Please provide a valid member_id value",
                )

            member_helper = HelperMember(
                request_context=request_context, environ_context=environ_context
            )
            member_update = member_helper.get_reference_id(body_json["member"]["id"])

            if isinstance(member_update, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            _check_input_attributes(body_json, member_update)

            response = member_helper.update(
                member_update=member_update,
                owner_member_id=body_json["owner_member_id"],
            )

            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "OK",
                    "message": "Request was received",
                    "data": {
                        "id": response.reference_id,
                        "auth_id": response.auth_id,
                        "child_id": response.child_id,
                        "email": response.email,
                        "first_name": response.first_name,
                        "last_name": response.last_name,
                        "avatar": response.avatar,
                        "role": response.role,
                        "invite": response.invite,
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


@BLUEPRINT_MEMBER.route("", methods=["POST"])
def post() -> Response:
    """
    Process POST request for the /member endpoint
    Update a member
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing POST request for MEMBER member")
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

            if body_json["email"] is None:
                LOGGER.logger.error("Missing email URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing email URL query. Please provide a valid email value",
                )

            member_helper = HelperMember(
                request_context=request_context, environ_context=environ_context
            )
            response = {}
            email = body_json["email"]
            owner = body_json["owner_member_id"]

            if "role" in body_json and body_json["role"] is not None:
                response = member_helper.invite(
                    {
                        "owner": owner,
                        "email": email,
                        "role": body_json["role"],
                        "first_name": body_json["first_name"],
                        "last_name": body_json["last_name"],
                    },
                )

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": response["status"],
                "message": response["message"],
                "data": {},
            },
            response["code"],
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


def _check_input_attributes(body_json, member):
    # if "email" in body_json["member"]:
    #     member.email = body_json["member"]["email"]

    if "first_name" in body_json["member"]:
        member.first_name = body_json["member"]["first_name"]

    if "last_name" in body_json["member"]:
        member.last_name = body_json["member"]["last_name"]

    if "avatar" in body_json["member"]:
        member.avatar = body_json["member"]["avatar"]

    if "role" in body_json["member"]:
        member.role = body_json["member"]["role"]
