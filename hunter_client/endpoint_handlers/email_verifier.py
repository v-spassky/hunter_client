"""This module contains handler class implementation for the `email-verifier` endpoint of the Hunter API."""

import requests

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler


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
        target_url = self._formatted_url(email=email)
        response = self._http_session.get(target_url)
        if response.status_code != requests.codes.ok:
            self._dispatch_client_exception(response)
        return response.json()['data']['status'] == 'valid'