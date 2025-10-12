# SPDX-License-Identifier: MIT
"""
Logger Factory
Author: snow-man-1
"""

import logging
from pathlib import Path


class LoggerFactory:
    _setup_finished = False

    @classmethod
    def setup_logger(cls, debug: bool = False) -> None:
        if cls._setup_finished:
            return

        log_level = logging.DEBUG if debug else logging.INFO

        log_file_directory = Path.home() / ".local" / "share" / "homelab-devtools"

        # make sure the path exists
        log_file_directory.mkdir(parents=True, exist_ok=True)

        main_log_file = log_file_directory / "app.log"

        file_handler = logging.FileHandler(main_log_file)
        file_handler.setLevel(log_level)

        log_formatter = logging.Formatter(
            "%(asctime)s %(name)s %(levelname)s %(message)s"
        )

        file_handler.setFormatter(log_formatter)

        main_logger = logging.getLogger()
        main_logger.setLevel(log_level)
        main_logger.addHandler(file_handler)

        cls._setup_finished = True

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        return logging.getLogger(name)
