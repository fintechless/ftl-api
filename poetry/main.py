"""
Poetry scripts, defined in pyproject.toml
"""

import os
import subprocess
import sys

import pytest

FILE_ABS_PATH: str = __file__
PROJECT_ABS_PATH: str = os.path.dirname(os.path.dirname(FILE_ABS_PATH))


def run_tests() -> None:
    """
    Run pytest tests
    """

    sys.exit(pytest.main(["-v"]))


def run_format() -> None:
    """
    Run black code formatter
    """

    subprocess.run(
        ["black", "."],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=PROJECT_ABS_PATH,
        check=False,
    )

    subprocess.run(
        ["isort", "."],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=PROJECT_ABS_PATH,
        check=False,
    )

    print("All done! ✨ 🍰 ✨")


def run_lint() -> None:
    """
    Run pylint
    """

    proc = subprocess.run(
        ["pylint ftl_api/**"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=PROJECT_ABS_PATH,
        check=False,
        shell=True,
    )

    print(proc.stdout.decode())
    print(proc.stderr.decode())
