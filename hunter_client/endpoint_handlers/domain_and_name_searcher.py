"""This module contains handler class implementation for the `email-finder` endpoint of the Hunter API."""

import requests

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler


class DomainAndNameSearcher(AbstractBaseEndpointHandler):
    """Handler for the `email-finder` endpoint in the Hunter API."""

    _endpoint_url_path = '/email-finder'

    def search_email_by_domain_and_name(self, target_domain: str, first_name: str, last_name: str) -> str | None:
        """
        Search for emails associated with a given domain.

        Args:
            target_domain (str): The domain to search emails for.

        Returns:
            list[str]: A list of email addresses found under the specified domain.
        """
        target_url = self._formatted_url(domain=target_domain, first_name=first_name, last_name=last_name)
        response = self._http_session.get(target_url)
        if response.status_code != requests.codes.ok:
            self._dispatch_client_exception(response)
        return response.json()['data']['email']
