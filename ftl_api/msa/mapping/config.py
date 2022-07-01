"""
Flask environment configuration
"""

import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


# pylint: disable=R0903
# Too few public methods (0/2) (too-few-public-methods)
class Config:
    """
    Base CONFIG class
    :param DEBUG
    :type DEBUG: bool
    """

    DEBUG = False
    SECRET_KEY = "fintechless"


# pylint: disable=R0903
# Too few public methods (0/2) (too-few-public-methods)
class DefaultConfig(Config):
    """
    CONFIG for default environment
    :param ENV
    :type ENV: str
    :param DEBUG
    :type DEBUG: bool
    """

    ENV = "default"
    DEBUG = True
