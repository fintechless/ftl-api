"""
Flask view for the UUID blueprint
Path: /
"""

from flask import Response
from flask import make_response
from flask import session
from ftl_python_lib.core.context.environment import EnvironmentContext
from ftl_python_lib.core.context.request import REQUEST_CONTEXT_SESSION
from ftl_python_lib.core.context.request import RequestContext
from ftl_python_lib.core.log import LOGGER
from ftl_python_lib.models.transaction import ModelTransaction
from ftl_python_lib.typings.models.transaction import TypeTransaction

from ftl_api.msa.uuid.blueprints import BLUEPRINT_UUID


@BLUEPRINT_UUID.route("", methods=["POST"])
def post() -> Response:
    """
    Process POST request for the /uuid endpoint
    Initiate a transaction
    """

    request_context: RequestContext = session.get(REQUEST_CONTEXT_SESSION)
    environ_context: EnvironmentContext = EnvironmentContext()

    LOGGER.logger.info("Proccessing POST request for UUID microservice")
    LOGGER.logger.info(f"Request ID is {request_context.request_id}")
    LOGGER.logger.info(f"Request timestamp is {request_context.requested_at_isoformat}")
    LOGGER.logger.info(f"Deployment ID is {environ_context.deployment_id}")
    LOGGER.logger.info(f"Database password is {environ_context.ftl_db_password}")

    transaction_model: ModelTransaction = ModelTransaction(
        request_context=request_context, environ_context=environ_context
    )

    initiated: TypeTransaction = transaction_model.initiate()

    return make_response(
        {
            "request_id": request_context.request_id,
            "transaction_id": initiated.transaction_id,
            "status": "OK",
        },
        200,
    )
