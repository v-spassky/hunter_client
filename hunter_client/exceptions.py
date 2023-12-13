"""This module declares all possible exceptions that can be raised by the `hunter_client` library."""


class HunterError(Exception):
    """Base class for all exceptions raised by the `hunter_client` library."""


class TooManyRequestsError(HunterError):
    """Exception raised when the Hunter API returns a 429 response."""


class InvalidInputError(HunterError):
    """Exception raised when the Hunter API returns a 400 response."""


class HunterServerError(HunterError):
    """Exception raised when the Hunter API returns a 500 response."""
