"""
Flask view for the TRANSACTION_TYPE blueprint
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
from ftl_python_lib.models.sql.transaction_type import ModelTransactionType
from ftl_python_lib.models_helper.transaction_type import HelperTransactionType
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.transaction_type.blueprints import BLUEPRINT_TRANSACTION_TYPE


@BLUEPRINT_TRANSACTION_TYPE.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /transaction_type endpoint
    Retrieve transaction_type for a given transaction_type_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for TRANSACTION_TYPE transaction_type")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    transaction_type_id: str = request.args.get("transaction_type_id")

    try:
        transaction_type_helper = HelperTransactionType(
            request_context=request_context, environ_context=environ_context
        )
        data = {}
        if transaction_type_id is None:
            transaction_type_list = transaction_type_helper.get_all()
            transaction_type_response = []
            for transaction_type in transaction_type_list:
                transaction_type_response.append(
                    {
                        "id": transaction_type.reference_id,
                        "child_id": transaction_type.child_id,
                        "name": transaction_type.name,
                        "object_type": transaction_type.object_type,
                    }
                )
            data = transaction_type_response
        else:
            transaction_type = transaction_type_helper.get_by_reference_id(
                transaction_type_id
            )
            if isinstance(transaction_type) == NoneType:
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            data = {
                "id": transaction_type.reference_id,
                "child_id": transaction_type.child_id,
                "name": transaction_type.name,
                "object_type": transaction_type.object_type,
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


@BLUEPRINT_TRANSACTION_TYPE.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /transaction_type endpoint
    Update a transaction_type
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing PATCH request for TRANSACTION_TYPE transaction_type"
    )
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

            if body_json["transaction_type"]["id"] is None:
                LOGGER.logger.error("Missing transaction_type URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing transaction_type_id URL query. Please provide a valid transaction_type_id value",
                )

            transaction_type_helper = HelperTransactionType(
                request_context=request_context, environ_context=environ_context
            )
            transaction_type_update = transaction_type_helper.get_by_reference_id(
                body_json["transaction_type"]["id"]
            )

            if isinstance(transaction_type_update, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            _check_input_attributes(body_json, transaction_type_update)

            response = transaction_type_helper.update(
                transaction_type_update=transaction_type_update,
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
                        "object_type": response.object_type,
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


def _check_input_attributes(body_json, transaction_type):
    if "type_id" in body_json["transaction_type"]:
        transaction_type.type_id = body_json["transaction_type"]["type_id"]

    if "name" in body_json["transaction_type"]:
        transaction_type.name = body_json["transaction_type"]["name"]

    if "object_type" in body_json["transaction_type"]:
        transaction_type.object_type = body_json["transaction_type"]["object_type"]


@BLUEPRINT_TRANSACTION_TYPE.route("", methods=["POST"])
def post() -> Response:
    """
    Process PATCH request for the /transaction_type endpoint
    Create new transaction_type
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing PATCH request for TRANSACTION_TYPE transaction_type"
    )
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

            if body_json["transaction_type"] is None:
                LOGGER.logger.error("Missing transaction_type URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
                )

            transaction_type_new: ModelTransactionType = ModelTransactionType(
                name=body_json["transaction_type"]["name"]
            )

            _check_input_attributes(body_json, transaction_type_new)

            transaction_type_helper = HelperTransactionType(
                request_context=request_context, environ_context=environ_context
            )

            transaction_type_exist = transaction_type_helper.get_by_name(
                transaction_type_new.name
            )
            if transaction_type_exist is not None:
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "OK",
                        "message": "This transaction_type exists.",
                        "data": {},
                    },
                    400,
                )

            response = transaction_type_helper.create(
                transaction_type_new=transaction_type_new,
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
                        "object_type": response.object_type,
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


@BLUEPRINT_TRANSACTION_TYPE.route("", methods=["DELETE"])
def delete() -> Response:
    """
    Process GET request for the /transaction_type endpoint
    Delete transaction_type for a given transaction_type_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for TRANSACTION_TYPE transaction_type")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    if request.args.get("transaction_type_id") is None:
        LOGGER.logger.error("Missing transaction_type_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing transaction_type_id URL query. Please provide a valid transaction_type_id value",
        )

    transaction_type_id: str = request.args.get("transaction_type_id")

    if request.args.get("owner_member_id") is None:
        LOGGER.logger.error("Missing owner_member_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
        )

    owner_member_id: str = request.args.get("owner_member_id")

    try:
        transaction_type_helper = HelperTransactionType(
            request_context=request_context, environ_context=environ_context
        )
        transaction_type_exist = transaction_type_helper.get_by_reference_id(
            transaction_type_id
        )

        if isinstance(transaction_type_exist, NoneType):
            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "Not found",
                    "message": 'This id doesn"t exist',
                },
                404,
            )

        transaction_type_helper.delete_by_id(owner_member_id, transaction_type_id)

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "TransactionType was deleted",
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
