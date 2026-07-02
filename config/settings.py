""" Shared configuration for the AI Testing Framework. """

from pathlib import Path


# Project directories

PROJECT_ROOT = Path(__file__).resolve().parent.parent

REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"
SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"


# Test execution

DEFAULT_TIMEOUT = 30


# Logging

LOG_LEVEL = "INFO"