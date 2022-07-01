"""
Member MEMBER
"""

import os

from flask import Flask
from flask_cors import CORS
from ftl_python_lib.core.context.environment import push_environ_to_os
# pylint: disable=W0611:
# unused-import
from prometheus_flask_exporter import PrometheusMetrics

from ftl_api.mgr.member import config

CONFIGURATION_SETUP: str = os.environ.get("CONFIGURATION_SETUP", "")


def create_app(test_config=None) -> Flask:
    """Create and configure an instance of the Flask application."""

    app = Flask(__name__, instance_relative_config=True)

    # Init Environment Context
    push_environ_to_os()
    CORS(app)

    app.config.from_mapping(
        # a default secret that should be overridden by instance config
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(CONFIGURATION_SETUP)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # apply the blueprints to the app
    # pylint: disable=C0415
    # pylint: disable=W0611
    import ftl_api.mgr.member.views
    from ftl_api.mgr.member.blueprints import BLUEPRINT_MEMBER

    app.register_blueprint(BLUEPRINT_MEMBER)

    metrics = PrometheusMetrics.for_app_factory()
    metrics.init_app(app)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    # app.add_url_rule("/", endpoint="index")

    return app
