"""Utility functions for working with files and directories."""

from pathlib import Path


def create_directory(directory: Path) -> None:
    """
    Create a directory if it does not already exist.

    Args:
        directory: Directory to create.
    """

    directory.mkdir(parents=True, exist_ok=True)