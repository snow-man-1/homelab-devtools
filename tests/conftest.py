# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

# Standard Imports
import logging
from collections.abc import Generator

# Third Party Imports
import pytest

# Project Imports
from homelab_devtools.logger_factory import LoggerFactory


@pytest.fixture
def logger_factory() -> Generator[LoggerFactory, None, None]:
    reset_logger_factory()
    yield LoggerFactory
    reset_logger_factory()


def reset_logger_factory():
    LoggerFactory._setup_finished = False
    logging.getLogger().handlers.clear()
