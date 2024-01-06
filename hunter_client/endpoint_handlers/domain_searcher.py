"""This module contains handler class implementation for the `domain-search` endpoint of the Hunter API."""

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler
from hunter_client.endpoint_handlers.mappers import DomainMapper
from hunter_client.endpoint_handlers.presenters import DomainPresenter
from hunter_client.endpoint_handlers.response_models import DomainSearcherResponse


class DomainSearcher(AbstractBaseEndpointHandler):
    """
    Handler for the `domain-search` endpoint in the Hunter API.

    Wraps this endpoint: https://hunter.io/api-documentation/v2#domain-search.
    """

    _endpoint_url_path = '/domain-search'

    def search_emails_by_domain(self, target_domain: str) -> list[str]:
        """
        Search for emails associated with a given domain.

        Args:
            target_domain (str): The domain to search emails for.

        Returns:
            list[str]: A list of email addresses found under the specified domain.
        """
        response = self.make_request('GET', domain=target_domain)
        response_body = DomainSearcherResponse.model_validate(response.json())
        domain = DomainMapper.from_domain_searcher_response(response_body)
        return DomainPresenter(domain).bare_email_addresses()
