"""This module contains handler class implementation for the `email-count` endpoint of the Hunter API."""

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler


class EmailCounter(AbstractBaseEndpointHandler):
    """
    Handler for the `email-count` endpoint in the Hunter API.

    Wraps this endpoint: https://hunter.io/api-documentation/v2#email-count.
    """

    _endpoint_url_path = '/email-count'

    def count_emails_by_domain(self, target_domain: str) -> dict:
        """
        Count the number of emails associated with a given domain.

        Args:
            target_domain (str): The domain to count emails for.

        Returns:
            dict: Raw JSON response from the wrapped API endpoint (`.../email-count`).
        """
        return self.make_request('GET', domain=target_domain).json()
