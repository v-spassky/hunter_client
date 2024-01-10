"""
This module provides a client for interacting with the Hunter API.

The HunterClient class defined in this module allows users to perform various actions related to email hunting,
such as searching for emails by domain, finding specific emails using a person's name and domain, verifying the
status of an email address, and counting the number of emails associated with a particular domain.
"""

import requests

from hunter_client.endpoint_handlers.domain_and_name_searcher import DomainAndNameSearcher
from hunter_client.endpoint_handlers.domain_searcher import DomainSearcher
from hunter_client.endpoint_handlers.email_counter import EmailCounter
from hunter_client.endpoint_handlers.email_verifier import EmailVerifier


class HunterClient(object):
    """
    Client for interacting with the Hunter.io API via HTTP requests.

    This class exposes functionality of the Hunter.io API endpoints.
    See https://hunter.io/api-documentation/v2 for more information.
    """

    _hunter_domain = 'https://api.hunter.io/v2'

    def __init__(
        self,
        api_key: str,
        http_session: requests.Session | None = None,
    ) -> None:
        """
        Initialize a new instance of the HunterClient class.

        Args:
            api_key (str): The API key for accessing the Hunter.io API.
            http_session (requests.Session | None): The HTTP session to use for making requests.
        """
        self._api_key = api_key
        self.http_session = http_session or requests.Session()
        self.http_session.headers.update({'X-API-KEY': self._api_key})
        self.domain_searcher = DomainSearcher(client=self)
        self.domain_and_name_searcher = DomainAndNameSearcher(client=self)
        self.email_verifier = EmailVerifier(client=self)
        self.email_counter = EmailCounter(client=self)
