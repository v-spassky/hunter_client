"""This module contains handler class implementation for the `domain-search` endpoint of the Hunter API."""

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler


class DomainSearcher(AbstractBaseEndpointHandler):
    """
    Handler for the `domain-search` endpoint in the Hunter API.

    Wraps this endpoint: https://hunter.io/api-documentation/v2#domain-search.
    """

    _endpoint_url_path = '/domain-search'

    def search_emails_by_domain(self, target_domain: str) -> dict:
        """
        Search for emails associated with a given domain.

        Args:
            target_domain (str): The domain to search emails for.

        Returns:
            dict: Raw JSON response from the wrapped API endpoint (`.../domain-search`).
        """
        return self.make_request('GET', domain=target_domain).json()
