"""
Flask view for the TRANSACTION blueprint
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
from ftl_python_lib.models.sql.transaction import ModelTransaction
from ftl_python_lib.models_helper.transaction import HelperTransaction
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.transaction.blueprints import BLUEPRINT_TRANSACTION


@BLUEPRINT_TRANSACTION.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /transaction endpoint
    Retrieve transaction for a given transaction_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for TRANSACTION transaction")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    transaction_id: str = request.args.get("transaction_id")

    try:
        transaction_helper = HelperTransaction(
            request_context=request_context, environ_context=environ_context
        )
        data = {}
        if transaction_id is None:
            transaction_list = transaction_helper.get_all()
            transaction_response = []
            for transaction in transaction_list:
                transaction_response.append(
                    {
                        "id": transaction.reference_id,
                        "child_id": transaction.child_id,
                        "type_id": transaction.type_id,
                        "active": transaction.active,
                        "name": transaction.name,
                        "description": transaction.description,
                    }
                )
            data = transaction_response
        else:
            transaction = transaction_helper.get_by_reference_id(transaction_id)
            if isinstance(transaction, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            data = {
                "id": transaction.reference_id,
                "child_id": transaction.child_id,
                "type_id": transaction.type_id,
                "active": transaction.active,
                "name": transaction.name,
                "description": transaction.description,
                "microservices": transaction.microservices,
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


@BLUEPRINT_TRANSACTION.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /transaction endpoint
    Update a transaction
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for TRANSACTION transaction")
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

            if body_json["transaction"]["id"] is None:
                LOGGER.logger.error("Missing transaction URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing transaction_id URL query. Please provide a valid transaction_id value",
                )

            transaction_helper = HelperTransaction(
                request_context=request_context, environ_context=environ_context
            )
            transaction_update = transaction_helper.get_by_reference_id(
                body_json["transaction"]["id"], True
            )

            if isinstance(transaction_update, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            _check_input_attributes(body_json, transaction_update)

            response = transaction_helper.update(
                transaction_update=transaction_update,
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
                        "type_id": response.type_id,
                        "name": response.name,
                        "description": response.description,
                        "active": response.active,
                        "microservices": response.microservices,
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


def _check_input_attributes(body_json, transaction):
    if "type_id" in body_json["transaction"]:
        transaction.type_id = body_json["transaction"]["type_id"]

    if "name" in body_json["transaction"]:
        transaction.name = body_json["transaction"]["name"]

    if "description" in body_json["transaction"]:
        transaction.description = body_json["transaction"]["description"]

    if "active" in body_json["transaction"]:
        transaction.active = body_json["transaction"]["active"]

    # if isinstance(transaction.active, type(True)):
    #     transaction.active = str(transaction.active).lower()

    if transaction.active is None:
        transaction.active = False

    if "microservices" in body_json["transaction"]:
        transaction.microservices = body_json["transaction"]["microservices"]

    if transaction.microservices is None:
        transaction.microservices = ["b14a5198-be76-4519-be17-6e6fc9f3f475"]


@BLUEPRINT_TRANSACTION.route("", methods=["POST"])
def post() -> Response:
    """
    Process PATCH request for the /transaction endpoint
    Create new transaction
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for TRANSACTION transaction")
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

            if body_json["transaction"] is None:
                LOGGER.logger.error("Missing transaction URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
                )

            transaction_new: ModelTransaction = ModelTransaction(
                name=body_json["transaction"]["name"]
            )

            _check_input_attributes(body_json, transaction_new)

            transaction_helper = HelperTransaction(
                request_context=request_context, environ_context=environ_context
            )

            transaction_exist = transaction_helper.get_by_name(transaction_new.name)
            if transaction_exist is not None:
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "OK",
                        "message": "This transaction exists.",
                        "data": {},
                    },
                    400,
                )

            response = transaction_helper.create(
                transaction_new=transaction_new,
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
                        "active": response.active,
                        "description": response.description,
                        "type_id": response.type_id,
                        "microservices": response.microservices,
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


@BLUEPRINT_TRANSACTION.route("", methods=["DELETE"])
def delete() -> Response:
    """
    Process GET request for the /transaction endpoint
    Delete transaction for a given transaction_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for TRANSACTION transaction")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    if request.args.get("transaction_id") is None:
        LOGGER.logger.error("Missing transaction_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing transaction_id URL query. Please provide a valid transaction_id value",
        )

    transaction_id: str = request.args.get("transaction_id")

    if request.args.get("owner_member_id") is None:
        LOGGER.logger.error("Missing owner_member_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
        )

    owner_member_id: str = request.args.get("owner_member_id")

    try:
        transaction_helper = HelperTransaction(
            request_context=request_context, environ_context=environ_context
        )
        transaction_helper.delete_by_id(owner_member_id, transaction_id)

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "Transaction was deleted",
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
