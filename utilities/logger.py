"""
Shared logging utilities for the AI Testing Framework.

This module provides a reusable logger that can be used by any AI
application built on top of the framework.
"""

import logging

from config.settings import LOG_LEVEL, LOGS_DIR
from utilities.file_manager import create_directory


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Args:
        name: Name of the logger.

    Returns:
        A configured Logger instance.
    """

    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    create_directory(LOGS_DIR)

    file_handler = logging.FileHandler(
        LOGS_DIR / "framework.log",
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger