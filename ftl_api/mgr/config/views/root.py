"""
Flask view for the CONFIG blueprint
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
from ftl_python_lib.models.sql.config import ModelConfig
from ftl_python_lib.models.sql.provider import ModelProvider
from ftl_python_lib.models_helper.config import HelperConfig
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.config.blueprints import BLUEPRINT_CONFIG


@BLUEPRINT_CONFIG.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /mgr/config endpoint
    Retrieve config for a given config_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for CONFIG config")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    config_id: str = request.args.get("config_id")

    try:
        config_helper = HelperConfig(
            request_context=request_context, environ_context=environ_context
        )
        data = NoneType
        if config_id is None:
            config_response = []
            config_list = config_helper.get_all()
            for config in config_list:
                config_response.append(
                    {
                        "id": config.reference_id,
                        "active": config.active,
                        "activated_at": config.activated_at,
                        "var_key": config.var_key,
                        "var_value": config.var_value,
                    }
                )
            data = config_response
        else:
            config = config_helper.get_by_reference_id(config_id)

            if isinstance(config, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            data = {
                "id": config.reference_id,
                "active": config.active,
                "activated_at": config.activated_at,
                "var_key": config.var_key,
                "var_value": config.var_value,
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


@BLUEPRINT_CONFIG.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /mgr/config endpoint
    Update a config
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for CONFIG config")
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw config
    config_raw: Union[bytes, str] = request.data

    try:
        if len(config_raw) == 0 or config_raw is None:
            LOGGER.logger.error("Missing config body")
            raise ExceptionInvalidRequest(
                message="Missing config body", request_context=request_context
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

            if body_json["config"]["id"] is None:
                LOGGER.logger.error("Missing config URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing config_id URL query. Please provide a valid config_id value",
                )

            config_helper = HelperConfig(
                request_context=request_context, environ_context=environ_context
            )
            config_update = config_helper.get_reference_id(body_json["config"]["id"])

            if isinstance(config_update, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            _check_input_update_attributes(body_json, config_update)

            response = config_helper.update(
                config_update=config_update,
                owner_member_id=body_json["owner_member_id"],
            )

            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "OK",
                    "message": "Request was received",
                    "data": {
                        "id": response.reference_id,
                        "active": response.active,
                        "activated_at": response.activated_at,
                        "var_key": response.var_key,
                        "var_value": response.var_value,
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


def _check_input_attributes(body_json, config):
    _check_input_update_attributes(body_json, config)

    if "ref_key" in body_json["config"]:
        config.ref_key = body_json["config"]["ref_key"]
        config.ref_table = ModelProvider.__identifier__

    if "var_key" in body_json["config"]:
        config.var_key = body_json["config"]["var_key"]


def _check_input_update_attributes(body_json, config):
    if "active" in body_json["config"]:
        config.active = body_json["config"]["active"]

    if config.active is None:
        config.active = False

    if "description" in body_json["config"]:
        config.description = body_json["config"]["description"]

    if "activated_at" in body_json["config"]:
        config.activated_at = body_json["config"]["activated_at"]

    if "var_value" in body_json["config"]:
        config.var_value = body_json["config"]["var_value"]


@BLUEPRINT_CONFIG.route("", methods=["POST"])
def post() -> Response:
    """
    Process PATCH request for the /config endpoint
    Create new config
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for CONFIG config")
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw config
    config_raw: Union[bytes, str] = request.data

    try:
        if len(config_raw) == 0 or config_raw is None:
            LOGGER.logger.error("Missing config body")
            raise ExceptionInvalidRequest(
                message="Missing config body", request_context=request_context
            )

        if isinstance(request.data, bytes):
            body = bytes_to_str(src=request.data)
            body_json = json.loads(body)

            _check_params(request_context, body_json)

            config_new: ModelConfig = ModelConfig()

            _check_input_attributes(body_json, config_new)

            config_helper = HelperConfig(
                request_context=request_context, environ_context=environ_context
            )
            config_exist = config_helper.get_by_key(
                var_key=config_new.var_key,
                ref_table=config_new.ref_table,
                ref_key=config_new.ref_key,
            )

            if config_exist is not None:
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "OK",
                        "message": "This config exists.",
                        "data": {},
                    },
                    400,
                )
            response = config_helper.create(
                config_new=config_new, owner_member_id=body_json["owner_member_id"]
            )

            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "OK",
                    "message": "Request was received",
                    "data": {
                        "id": response.reference_id,
                        "active": response.active,
                        "activated_at": response.activated_at,
                        "var_key": response.var_key,
                        "var_value": response.var_value,
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

    if body_json["config"] is None:
        LOGGER.logger.error("Missing config URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing config URL query. Please provide a valid config value",
        )


@BLUEPRINT_CONFIG.route("", methods=["DELETE"])
def delete() -> Response:
    """
    Process GET request for the /config endpoint
    Delete config for a given config_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for CONFIG config")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    if request.args.get("config_id") is None:
        LOGGER.logger.error("Missing config_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing config_id URL query. Please provide a valid config_id value",
        )

    config_id: str = request.args.get("config_id")

    if request.args.get("owner_member_id") is None:
        LOGGER.logger.error("Missing owner_member_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
        )

    owner_member_id: str = request.args.get("owner_member_id")

    try:
        config_helper = HelperConfig(
            request_context=request_context, environ_context=environ_context
        )
        config_helper.delete_by_id(owner_member_id, config_id)

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "Config was deleted",
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
