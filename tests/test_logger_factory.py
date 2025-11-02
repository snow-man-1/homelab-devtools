# SPDX-License-Identifier: MIT
"""
Test class for Unit Testing the LoggerFactory class which setups a logger with file and format handling
Author: snow-man-1
"""

import logging

from homelab_devtools.logger_factory import LoggerFactory


class TestLoggerFactory:
    def test_logger_setup_with_info_level(
        self,
        logger_factory: LoggerFactory,
    ):
        logger_factory.setup_logger()
        logger = logging.getLogger()
        assert logger.level == logging.INFO

    def test_logger_setup_with_debug_level(
        self,
        logger_factory: LoggerFactory,
    ):
        logger_factory.setup_logger(debug=True)
        logger = logging.getLogger()
        assert logger.level == logging.DEBUG

    def test_logger_factory_cannot_setup_twice(self, logger_factory: LoggerFactory):
        logger_factory.setup_logger()
        first_logger = logging.getLogger()
        num_handlers_first_logger = len(first_logger.handlers)

        # second setup
        logger_factory.setup_logger()
        second_logger = logging.getLogger()
        num_handlers_second_logger = len(second_logger.handlers)

        assert num_handlers_first_logger == num_handlers_second_logger

    def test_get_logger_of_factory(self, logger_factory: LoggerFactory):
        LoggerFactory.setup_logger()
        logger = LoggerFactory.get_logger("test_logger")

        assert logger.name == "test_logger"
