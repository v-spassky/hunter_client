"""This module contains handler class implementation for the `email-finder` endpoint of the Hunter API."""

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler


class DomainAndNameSearcher(AbstractBaseEndpointHandler):
    """
    Handler for the `email-finder` endpoint in the Hunter API.

    Wraps this endpoint: https://hunter.io/api-documentation/v2#email-finder.
    """

    _endpoint_url_path = '/email-finder'

    def search_email_by_domain_and_name(self, target_domain: str, first_name: str, last_name: str) -> dict:
        """
        Search for emails associated with a given domain and name.

        Args:
            target_domain (str): The domain to search emails for.
            first_name (str): The first name of the person to search for.
            last_name (str): The last name of the person to search for.

        Returns:
            dict: Raw JSON response from the wrapped API endpoint (`.../email-finder`).
        """
        return self.make_request('GET', domain=target_domain, first_name=first_name, last_name=last_name).json()
