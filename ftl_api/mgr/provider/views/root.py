"""
Flask view for the PROVIDER blueprint
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
from ftl_python_lib.models.sql.provider import ModelProvider
from ftl_python_lib.models_helper.config import HelperConfig
from ftl_python_lib.models_helper.provider import HelperProvider
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.provider.blueprints import BLUEPRINT_PROVIDER


@BLUEPRINT_PROVIDER.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /mgr/provider endpoint
    Retrieve provider for a given provider_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing GET request for PROVIDER provider")
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    provider_id: str = request.args.get("provider_id")
    provider_category_id: str = request.args.get("provider_category_id")
    provider_subcategory_id: str = request.args.get("provider_subcategory_id")

    try:
        provider_helper = HelperProvider(
            request_context=request_context, environ_context=environ_context
        )
        data = NoneType
        if provider_category_id is not None and provider_subcategory_id is not None:
            data = _get_provider_list(
                provider_helper.get_all_by_category_id_subcategory_id(
                    provider_category_id, provider_subcategory_id
                )
            )
        elif provider_id is None:
            data = _get_provider_list(provider_helper.get_all())
        else:
            provider = provider_helper.get_by_reference_id(provider_id)

            if isinstance(provider, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            data = {
                "id": provider.reference_id,
                "name": provider.name,
                "description": provider.description,
                "active": provider.active,
                "activated_at": provider.activated_at,
                "category_id": provider.category_id,
                "subcategory_id": provider.subcategory_id,
                "config": _get_config_list(provider),
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


def _get_config_list(provider):
    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()
    config_helper = HelperConfig(
        request_context=request_context, environ_context=environ_context
    )
    config_list = []
    for item in config_helper.get_all_by_identifier_id(
        ModelProvider.__identifier__, provider.reference_id, provider.secret_ref
    ):
        config_list.append(
            {
                "id": item.reference_id,
                "active": item.active,
                "activated_at": item.activated_at,
                "var_key": item.var_key,
                "var_value": item.var_value,
            }
        )

    return config_list


def _get_provider_list(provider_list):
    provider_response = []
    for provider in provider_list:
        provider_response.append(
            {
                "id": provider.reference_id,
                "name": provider.name,
                "description": provider.description,
                "active": provider.active,
                "activated_at": provider.activated_at,
                "category_id": provider.category_id,
                "subcategory_id": provider.subcategory_id,
                "config": _get_config_list(provider),
            }
        )
    return provider_response


@BLUEPRINT_PROVIDER.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /provider endpoint
    Update a provider
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing PATCH request for PROVIDER provider")
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

            if body_json["provider"] is None:
                LOGGER.logger.error("Missing provider URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing provider URL query. Please provide a valid provider value",
                )

            if body_json["provider"]["id"] is None:
                LOGGER.logger.error("Missing provider URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing provider_id URL query. Please provide a valid provider_id value",
                )

            provider_helper = HelperProvider(
                request_context=request_context, environ_context=environ_context
            )
            provider_exist = provider_helper.get_by_reference_id(
                body_json["provider"]["id"]
            )

            if isinstance(provider_exist, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            provider_update = ModelProvider(
                id=provider_exist.id,
                child_id=provider_exist.id,
                reference_id=provider_exist.reference_id,
                name=provider_exist.name,
                activated_at=provider_exist.activated_at,
                active=provider_exist.active,
                description=provider_exist.description,
                category_id=provider_exist.category_id,
                subcategory_id=provider_exist.subcategory_id,
                created_by=provider_exist.created_by,
            )

            if "active" in body_json["provider"]:
                provider_update.active = body_json["provider"]["active"]

            response = provider_helper.update(
                provider_update=provider_update,
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
