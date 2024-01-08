"""This module contains handler class implementation for the `email-verifier` endpoint of the Hunter API."""

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler


class EmailVerifier(AbstractBaseEndpointHandler):
    """
    Handler for the `email-verifier` endpoint in the Hunter API.

    Wraps this endpoint: https://hunter.io/api-documentation/v2#email-verifier.
    """

    _endpoint_url_path = '/email-verifier'

    def check_if_email_is_valid(self, email: str) -> dict:
        """
        Verify the status of an email address.

        Args:
            email (str): The email address to verify.

        Returns:
            dict: Raw JSON response from the wrapped API endpoint (`.../email-verifier`).
        """
        return self.make_request('GET', email=email).json()
