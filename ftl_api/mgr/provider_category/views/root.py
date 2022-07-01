"""
Flask view for the PROVIDER_CATEGORY blueprint
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
from ftl_python_lib.models.sql.provider_category import ModelProviderCategory
from ftl_python_lib.models_helper.provider_category import HelperProviderCategory
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.provider_category.blueprints import BLUEPRINT_PROVIDER_CATEGORY


@BLUEPRINT_PROVIDER_CATEGORY.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /mgr/provider/category endpoint
    Retrieve provider_category for a given provider_category_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing GET request for PROVIDER_CATEGORY provider_category"
    )
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    provider_category_id: str = request.args.get("provider_category_id")

    try:
        provider_category_helper = HelperProviderCategory(
            request_context=request_context, environ_context=environ_context
        )
        data = NoneType
        if provider_category_id is None:
            data = []
            for provider_category in provider_category_helper.get_all():
                data.append(
                    {
                        "id": provider_category.reference_id,
                        "name": provider_category.name,
                        "description": provider_category.description,
                        "code": provider_category.code,
                    }
                )
        else:
            provider_category = provider_category_helper.get_by_reference_id(
                provider_category_id
            )

            if isinstance(provider_category, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            data = {
                "id": provider_category.reference_id,
                "name": provider_category.name,
                "description": provider_category.description,
                "code": provider_category.code,
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


@BLUEPRINT_PROVIDER_CATEGORY.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /mgr/provider/category endpoint
    Update a provider_category
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing PATCH request for PROVIDER_CATEGORY provider_category"
    )
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw provider_category
    provider_category_raw: Union[bytes, str] = request.data

    try:
        if len(provider_category_raw) == 0 or provider_category_raw is None:
            LOGGER.logger.error("Missing provider_category body")
            raise ExceptionInvalidRequest(
                message="Missing provider_category body",
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

            if body_json["provider_category"]["id"] is None:
                LOGGER.logger.error("Missing provider_category URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="""Missing provider_category_id URL query.
                        Please provide a valid provider_category_id value""",
                )

            provider_category_helper = HelperProviderCategory(
                request_context=request_context, environ_context=environ_context
            )
            provider_category_update = provider_category_helper.get_by_reference_id(
                body_json["provider_category"]["id"]
            )

            if isinstance(provider_category_update, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            _check_input_attributes(body_json, provider_category_update)

            response = provider_category_helper.update(
                provider_category_update=provider_category_update,
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


def _check_input_attributes(body_json, provider_category):
    if "name" in body_json["provider_category"]:
        provider_category.name = body_json["provider_category"]["name"]

    if "description" in body_json["provider_category"]:
        provider_category.description = body_json["provider_category"]["description"]


@BLUEPRINT_PROVIDER_CATEGORY.route("", methods=["POST"])
def post() -> Response:
    """
    Process PATCH request for the /provider_category endpoint
    Create new provider_category
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing PATCH request for PROVIDER_CATEGORY provider_category"
    )
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw provider_category
    provider_category_raw: Union[bytes, str] = request.data

    try:
        if len(provider_category_raw) == 0 or provider_category_raw is None:
            LOGGER.logger.error("Missing provider_category body")
            raise ExceptionInvalidRequest(
                message="Missing provider_category body",
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

            if body_json["provider_category"] is None:
                LOGGER.logger.error("Missing provider_category URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
                )

            provider_category_new: ModelProviderCategory = ModelProviderCategory(
                name=body_json["provider_category"]["name"]
            )

            _check_input_attributes(body_json, provider_category_new)

            provider_category_helper = HelperProviderCategory(
                request_context=request_context, environ_context=environ_context
            )

            provider_category_exist = provider_category_helper.get_by_name(
                provider_category_new.name
            )
            if provider_category_exist is not None:
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "OK",
                        "message": "This provider_category exists.",
                        "data": {},
                    },
                    400,
                )

            response = provider_category_helper.create(
                provider_category_new=provider_category_new,
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


@BLUEPRINT_PROVIDER_CATEGORY.route("", methods=["DELETE"])
def delete() -> Response:
    """
    Process GET request for the /provider_category endpoint
    Delete provider_category for a given provider_category_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing GET request for PROVIDER_CATEGORY provider_category"
    )
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    if request.args.get("provider_category_id") is None:
        LOGGER.logger.error("Missing provider_category_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message=(
                "Missing provider_category_id URL query."
                + "Please provide a valid provider_category_id value"
            ),
        )

    provider_category_id: str = request.args.get("provider_category_id")

    if request.args.get("owner_member_id") is None:
        LOGGER.logger.error("Missing owner_member_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
        )

    owner_member_id: str = request.args.get("owner_member_id")

    try:
        provider_category_helper = HelperProviderCategory(
            request_context=request_context, environ_context=environ_context
        )
        provider_category_exist = provider_category_helper.get_by_reference_id(
            provider_category_id
        )

        if isinstance(provider_category_exist, NoneType):
            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "Not found",
                    "message": 'This id doesn"t exist',
                },
                404,
            )

        provider_category_helper.delete_by_id(owner_member_id, provider_category_id)

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "ProviderCategory was deleted",
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
