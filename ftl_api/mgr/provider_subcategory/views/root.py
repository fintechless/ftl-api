"""
Flask view for the PROVIDER_SUBCATEGORY blueprint
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
from ftl_python_lib.models.sql.provider_subcategory import ModelProviderSubcategory
from ftl_python_lib.models_helper.provider_subcategory import HelperProviderSubcategory
from ftl_python_lib.utils.to_str import bytes_to_str

from ftl_api.mgr.provider_subcategory.blueprints import BLUEPRINT_PROVIDER_SUBCATEGORY


@BLUEPRINT_PROVIDER_SUBCATEGORY.route("", methods=["GET"])
def get() -> Response:
    """
    Process GET request for the /mgr/provider/subcategory endpoint
    Retrieve provider_subcategory for a given provider_subcategory_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing GET request for PROVIDER_SUBCATEGORY provider_subcategory"
    )
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    provider_category_id: str = request.args.get("provider_category_id")
    provider_subcategory_id: str = request.args.get("provider_subcategory_id")

    try:
        provider_subcategory_helper = HelperProviderSubcategory(
            request_context=request_context, environ_context=environ_context
        )
        data = NoneType
        if provider_category_id is not None:
            data = []
            for (
                provider_subcategory
            ) in provider_subcategory_helper.get_all_by_category_id(
                provider_category_id
            ):
                data.append(
                    {
                        "id": provider_subcategory.reference_id,
                        "name": provider_subcategory.name,
                        "description": provider_subcategory.description,
                        "code": provider_subcategory.code,
                    }
                )
        elif provider_subcategory_id is None:
            data = []
            for provider_subcategory in provider_subcategory_helper.get_all():
                data.append(
                    {
                        "id": provider_subcategory.reference_id,
                        "name": provider_subcategory.name,
                        "description": provider_subcategory.description,
                        "code": provider_subcategory.code,
                    }
                )
        else:
            provider_subcategory = provider_subcategory_helper.get_by_reference_id(
                provider_subcategory_id
            )

            if type(provider_subcategory, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            data = {
                "id": provider_subcategory.reference_id,
                "name": provider_subcategory.name,
                "description": provider_subcategory.description,
                "code": provider_subcategory.code,
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


@BLUEPRINT_PROVIDER_SUBCATEGORY.route("", methods=["PATCH"])
def patch() -> Response:
    """
    Process PATCH request for the /mgr/provider/subcategory endpoint
    Update a provider_subcategory
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing PATCH request for PROVIDER_SUBCATEGORY provider_subcategory"
    )
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw provider_subcategory
    provider_subcategory_raw: Union[bytes, str] = request.data

    try:
        if len(provider_subcategory_raw) == 0 or provider_subcategory_raw is None:
            LOGGER.logger.error("Missing provider_subcategory body")
            raise ExceptionInvalidRequest(
                message="Missing provider_subcategory body",
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

            if body_json["provider_subcategory"]["id"] is None:
                LOGGER.logger.error("Missing provider_subcategory URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="""Missing provider_subcategory_id URL query.
                        Please provide a valid provider_subcategory_id value""",
                )

            provider_subcategory_helper = HelperProviderSubcategory(
                request_context=request_context, environ_context=environ_context
            )
            provider_subcategory_update = (
                provider_subcategory_helper.get_by_reference_id(
                    body_json["provider_subcategory"]["id"]
                )
            )

            if isinstance(provider_subcategory_update, NoneType):
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "Not found",
                        "message": 'This id doesn"t exist',
                    },
                    404,
                )

            _check_input_attributes(body_json, provider_subcategory_update)

            response = provider_subcategory_helper.update(
                provider_subcategory_update=provider_subcategory_update,
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


def _check_input_attributes(body_json, provider_subcategory):
    if "name" in body_json["provider_subcategory"]:
        provider_subcategory.name = body_json["provider_subcategory"]["name"]

    if "description" in body_json["provider_subcategory"]:
        provider_subcategory.description = body_json["provider_subcategory"][
            "description"
        ]


@BLUEPRINT_PROVIDER_SUBCATEGORY.route("", methods=["POST"])
def post() -> Response:
    """
    Process PATCH request for the /provider_subcategory endpoint
    Create new provider_subcategory
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing PATCH request for PROVIDER_SUBCATEGORY provider_subcategory"
    )
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {request_context.requested_at_isoformat}")

    # Raw provider_subcategory
    provider_subcategory_raw: Union[bytes, str] = request.data

    try:
        if len(provider_subcategory_raw) == 0 or provider_subcategory_raw is None:
            LOGGER.logger.error("Missing provider_subcategory body")
            raise ExceptionInvalidRequest(
                message="Missing provider_subcategory body",
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

            if body_json["provider_subcategory"] is None:
                LOGGER.logger.error("Missing provider_subcategory URL query")
                raise ExceptionInvalidRequest(
                    request_context=request_context,
                    message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
                )

            provider_subcategory_new: ModelProviderSubcategory = (
                ModelProviderSubcategory(name=body_json["provider_subcategory"]["name"])
            )

            _check_input_attributes(body_json, provider_subcategory_new)

            provider_subcategory_helper = HelperProviderSubcategory(
                request_context=request_context, environ_context=environ_context
            )

            provider_subcategory_exist = provider_subcategory_helper.get_by_name(
                provider_subcategory_new.name
            )
            if provider_subcategory_exist is not None:
                return make_response(
                    {
                        "request_id": request_context.request_id,
                        "status": "OK",
                        "message": "This provider_subcategory exists.",
                        "data": {},
                    },
                    400,
                )

            response = provider_subcategory_helper.create(
                provider_subcategory_new=provider_subcategory_new,
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


@BLUEPRINT_PROVIDER_SUBCATEGORY.route("", methods=["DELETE"])
def delete() -> Response:
    """
    Process GET request for the /provider_subcategory endpoint
    Delete provider_subcategory for a given provider_subcategory_id
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info(
        "Proccessing GET request for PROVIDER_SUBCATEGORY provider_subcategory"
    )
    LOGGER.logger.info(f"FTL Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")

    if request.args.get("provider_subcategory_id") is None:
        LOGGER.logger.error("Missing provider_subcategory_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing provider_subcategory_id URL query. Please provide a valid provider_subcategory_id value",
        )

    provider_subcategory_id: str = request.args.get("provider_subcategory_id")

    if request.args.get("owner_member_id") is None:
        LOGGER.logger.error("Missing owner_member_id URL query")
        raise ExceptionInvalidRequest(
            request_context=request_context,
            message="Missing owner_member_id URL query. Please provide a valid owner_member_id value",
        )

    owner_member_id: str = request.args.get("owner_member_id")

    try:
        provider_subcategory_helper = HelperProviderSubcategory(
            request_context=request_context, environ_context=environ_context
        )
        provider_subcategory_exist = provider_subcategory_helper.get_by_reference_id(
            provider_subcategory_id
        )

        if isinstance(provider_subcategory_exist, NoneType):
            return make_response(
                {
                    "request_id": request_context.request_id,
                    "status": "Not found",
                    "message": 'This id doesn"t exist',
                },
                404,
            )

        provider_subcategory_helper.delete_by_id(
            owner_member_id, provider_subcategory_id
        )

        return make_response(
            {
                "request_id": request_context.request_id,
                "status": "OK",
                "message": "ProviderSubcategory was deleted",
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
