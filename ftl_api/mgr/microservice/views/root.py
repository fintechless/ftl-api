"""
Flask view for the MICROSERVICE blueprint
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
from ftl_python_lib.models.sql.microservice import ModelMicroservice
from ftl_python_lib.models_helper.microservice import HelperMicroservice
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.microservice.blueprints import BLUEPRINT_MICROSERVICE


@BLUEPRINT_MICROSERVICE.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /microservice endpoint
    Retrieve microservice for a given microservice_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for MICROSERVICE microservice")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    microservice_id: str = request.args.get("microservice_id")

    try:
        microservice_helper = HelperMicroservice(
            request_context=request_context, environ_context=environ_context
        )
        data = {}
        if microservice_id is None:
            microservice_list = microservice_helper.get_all()
            microservice_response = []
            for microservice in microservice_list:
                microservice_response.append(
                    {
                        "id": microservice.reference_id,
                        "name": microservice.name,
                        "active": microservice.active,
                        "description": microservice.description,
                        "path": microservice.path,
                        "runtime": microservice.runtime,
                    }
                )
            data = microservice_response
        else:
            microservice = microservice_helper.get_by_reference_id(microservice_id)

            if isinstance(microservice, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            data = {
                "id": microservice.reference_id,
                "name": microservice.name,
                "active": microservice.active,
                "description": microservice.description,
                "path": microservice.path,
                "runtime": microservice.runtime,
                "code": microservice.code,
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


@BLUEPRINT_MICROSERVICE.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /microservice endpoint
    Update a microservice
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for MICROSERVICE microservice")
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

            if body_json["microservice"] is None:
                LOGGER.logger.error("Missing microservice URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing microservice URL query. Please provide a valid microservice value",
                )

            if body_json["microservice"]["id"] is None:
                LOGGER.logger.error("Missing microservice URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing microservice_id URL query. Please provide a valid microservice_id value",
                )

            microservice_helper = HelperMicroservice(
                request_context=request_context, environ_context=environ_context
            )
            microservice_exist = microservice_helper.get_by_reference_id(
                body_json["microservice"]["id"]
            )

            if isinstance(microservice_exist, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            microservice_update = ModelMicroservice(
                id=microservice_exist.id,
                child_id=microservice_exist.id,
                reference_id=microservice_exist.reference_id,
                name=microservice_exist.name,
                active=microservice_exist.active,
                description=microservice_exist.description,
                path=microservice_exist.path,
                runtime=microservice_exist.runtime,
                code=microservice_exist.code,
                created_by=microservice_exist.created_by,
            )

            _check_input_attributes(body_json, microservice_update)

            microservice_bytes = base64.b64decode(body_json["microservice"]["content"]
                                                  ) if "content" in body_json["microservice"] else None
            file_path = body_json["microservice"]["file_path"] if "file_path" in body_json["microservice"] else None

            response = microservice_helper.update(
                microservice_update=microservice_update,
                owner_member_id=body_json["owner_member_id"],
                content=microservice_bytes,
                file_path=file_path,
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
                        "active": response.active,
                        "description": response.description,
                        "path": response.path,
                        "runtime": response.runtime,
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


def _check_input_attributes(body_json, microservice):
    if "name" in body_json["microservice"]:
        microservice.name = body_json["microservice"]["name"]

    if "active" in body_json["microservice"]:
        microservice.active = body_json["microservice"]["active"]

    if isinstance(microservice.active, type(True)):
        microservice.active = str(microservice.active).lower()

    if microservice.active is None:
        microservice.active = "false"

    if "description" in body_json["microservice"]:
        microservice.description = body_json["microservice"]["description"]

    if "path" in body_json["microservice"]:
        microservice.path = body_json["microservice"]["path"]

    if "runtime" in body_json["microservice"]:
        microservice.runtime = body_json["microservice"]["runtime"]


@BLUEPRINT_MICROSERVICE.route("", methods=["POST"])
def post() -> Response:
    """
    Process PATCH request for the /microservice endpoint
    Create new microservice
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for MICROSERVICE microservice")
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

            if body_json["microservice"] is None:
                LOGGER.logger.error("Missing microservice URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
                )

            microservice_new: ModelMicroservice = ModelMicroservice(
                name=body_json["microservice"]["name"],
                runtime=body_json["microservice"]["runtime"],
            )

            _check_input_attributes(body_json, microservice_new)

            microservice_helper = HelperMicroservice(
                request_context=request_context, environ_context=environ_context
            )

            microservice_exist = microservice_helper.get_by_name(microservice_new.name)
            if microservice_exist is not None:
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "OK",
                        "message": "This microservice exists.",
                        "data": {},
                    },
                    400,
                )

            response = microservice_helper.create(
                microservice_new=microservice_new,
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
                        "path": response.path,
                        "runtime": response.runtime,
                        "code": response.code,
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


@BLUEPRINT_MICROSERVICE.route("", methods=["DELETE"])
def delete() -> Response:
    """
    Process GET request for the /microservice endpoint
    Delete microservice for a given microservice_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for MICROSERVICE microservice")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    if request.args.get("microservice_id") is None:
        LOGGER.logger.error("Missing microservice_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing microservice_id URL query. Please provide a valid microservice_id value",
        )

    microservice_id: str = request.args.get("microservice_id")

    if request.args.get("owner_member_id") is None:
        LOGGER.logger.error("Missing owner_member_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
        )

    owner_member_id: str = request.args.get("owner_member_id")

    try:
        microservice_helper = HelperMicroservice(
            request_context=request_context, environ_context=environ_context
        )
        if microservice_helper.get_by_microservice_id(microservice_id) > 0:
            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "Precondition Required",
                    "message": "This request is required to be conditional",
                },
                428,
            )

        microservice_exist = microservice_helper.get_by_reference_id(microservice_id)

        if isinstance(microservice_exist, NoneType):
            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "Not found",
                    "message": 'This id doesn"t exist',
                },
                404,
            )

        microservice_helper.delete_by_id(owner_member_id, microservice_id)

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "Microservice was deleted",
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
