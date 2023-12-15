"""This module contains handler class implementation for the `email-finder` endpoint of the Hunter API."""

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler
from hunter_client.endpoint_handlers.response_models import DomainAndNameSearcherResponse


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
        response = self.make_request('GET', domain=target_domain, first_name=first_name, last_name=last_name)
        return DomainAndNameSearcherResponse.model_validate(response.json()['data']).email
