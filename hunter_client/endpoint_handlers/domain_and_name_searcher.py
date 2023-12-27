"""This module contains handler class implementation for the `email-finder` endpoint of the Hunter API."""

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler
from hunter_client.endpoint_handlers.mappers import EmailMapper
from hunter_client.endpoint_handlers.response_models import DomainAndNameSearcherResponse


class DomainAndNameSearcher(AbstractBaseEndpointHandler):
    """Handler for the `email-finder` endpoint in the Hunter API."""

    _endpoint_url_path = '/email-finder'

    def search_email_by_domain_and_name(self, target_domain: str, first_name: str, last_name: str) -> str | None:
        """
        Search for emails associated with a given domain and name.

        Args:
            target_domain (str): The domain to search emails for.
            first_name (str): The first name of the person to search for.
            last_name (str): The last name of the person to search for.

        Returns:
            str | None: The email address found, or None if no email was found.
        """
        response = self.make_request('GET', domain=target_domain, first_name=first_name, last_name=last_name)
        response_body = DomainAndNameSearcherResponse.model_validate(response.json())
        email = EmailMapper.from_domain_and_name_searcher_response(response_body)
        if not email:
            return None
        return email.address
