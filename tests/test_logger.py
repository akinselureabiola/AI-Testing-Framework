"""
Tests for the reusable logger.
"""

import logging

from utilities.logger import get_logger


def test_get_logger_returns_logger_instance():
    """
    Verify that get_logger() returns a Logger object.
    """

    logger = get_logger("test_logger")

    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_logger"