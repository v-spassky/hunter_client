"""This module contains handler class implementation for the `email-count` endpoint of the Hunter API."""

import requests

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler
from hunter_client.endpoint_handlers.response_models import EmailCounterResponse


class EmailCounter(AbstractBaseEndpointHandler):
    """Handler for the `email-count` endpoint in the Hunter API."""

    _endpoint_url_path = '/email-count'

    def count_emails_by_domain(self, target_domain: str) -> int:
        """
        Count the number of emails associated with a given domain.

        Args:
            target_domain (str): The domain to count emails for.

        Returns:
            int: The total number of emails found for the given domain.
        """
        target_url = self._formatted_url(domain=target_domain)
        response = self._http_session.get(target_url)
        if response.status_code != requests.codes.ok:
            self._dispatch_client_exception(response)
        return EmailCounterResponse.model_validate(response.json()['data']).total
