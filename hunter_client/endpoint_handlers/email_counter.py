"""This module contains handler class implementation for the `email-count` endpoint of the Hunter API."""

from hunter_client.endpoint_handlers.base import AbstractBaseEndpointHandler
from hunter_client.endpoint_handlers.mappers import DomainStatsMapper
from hunter_client.endpoint_handlers.response_models import EmailCounterResponse


class EmailCounter(AbstractBaseEndpointHandler):
    """
    Handler for the `email-count` endpoint in the Hunter API.

    Wraps this endpoint: https://hunter.io/api-documentation/v2#email-count.
    """

    _endpoint_url_path = '/email-count'

    def count_emails_by_domain(self, target_domain: str) -> int:
        """
        Count the number of emails associated with a given domain.

        Args:
            target_domain (str): The domain to count emails for.

        Returns:
            int: The total number of emails found for the given domain.
        """
        response = self.make_request('GET', domain=target_domain)
        response_body = EmailCounterResponse.model_validate(response.json())
        domain_stats = DomainStatsMapper.from_email_counter_response(response_body)
        return domain_stats.total_emails_count
