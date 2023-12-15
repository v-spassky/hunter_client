"""This module contains handler class implementation for the `email-verifier` endpoint of the Hunter API."""

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler
from hunter_client.endpoint_handlers.response_models import EmailVerifierResponse


class EmailVerifier(AbstractBaseEndpointHandler):
    """Handler for the `email-verifier` endpoint in the Hunter API."""

    _endpoint_url_path = '/email-verifier'

    def check_if_email_is_valid(self, email: str) -> bool:
        """
        Verify the status of an email address.

        Args:
            email (str): The email address to verify.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        response = self.make_request('GET', email=email)
        return EmailVerifierResponse.model_validate(response.json()['data']).is_valid
