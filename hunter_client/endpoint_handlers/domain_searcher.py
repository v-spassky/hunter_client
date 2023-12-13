"""This module contains handler class implementation for the `domain-search` endpoint of the Hunter API."""

import requests

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler
from hunter_client.endpoint_handlers.response_models import DomainSearcherResponse


class DomainSearcher(AbstractBaseEndpointHandler):
    """Handler for the `domain-search` endpoint in the Hunter API."""

    _endpoint_url_path = '/domain-search'

    def search_emails_by_domain(self, target_domain: str) -> list[str]:
        """
        Search for emails associated with a given domain.

        Args:
            target_domain (str): The domain to search emails for.

        Returns:
            list[str]: A list of email addresses found under the specified domain.
        """
        target_url = self._formatted_url(domain=target_domain)
        response = self._http_session.get(target_url)
        if response.status_code != requests.codes.ok:
            self._dispatch_client_exception(response)
        return DomainSearcherResponse.model_validate(response.json()['data']).bare_emails
