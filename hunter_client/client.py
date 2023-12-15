"""
This module provides a client for interacting with the Hunter API.

The HunterClient class defined in this module allows users to perform various actions related to email hunting,
such as searching for emails by domain, finding specific emails using a person's name and domain, verifying the
status of an email address, and counting the number of emails associated with a particular domain.

The client requires an API key for the Hunter service and offers the option to set a custom timeout for requests.
Each method in the HunterClient class makes a specific request to the Hunter API and handles the response
accordingly, providing a user-friendly interface for interacting with the Hunter API.

Classes:
    HunterClient: A client for interacting with the Hunter API.

Usage:
    To use the HunterClient, instantiate it with your Hunter API key and optionally specify a request timeout.
    Then, call its methods with the appropriate parameters to perform email searches, verifications, and counts.
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
    _default_request_timeout = 5

    def __init__(
        self,
        api_key: str,
        request_timeout: int | None = None,
        http_session: requests.Session | None = None,
    ) -> None:
        """
        Initialize a new instance of the HunterClient class.

        Args:
            api_key (str): The API key for accessing the Hunter.io API.
            request_timeout (int | None, optional): The timeout in seconds for API requests, defaults to None.
        """
        self._api_key = api_key
        self._request_timeout = request_timeout or self._default_request_timeout
        self._http_session = http_session or requests.Session()
        self._http_session.headers.update({'X-API-KEY': self._api_key})

    def search_emails_by_domain(self, target_domain: str) -> list[str]:
        """
        Search for emails associated with a given domain.

        Delegates the search for emails associated with a given domain to the `DomainSearcher`.

        Args:
            target_domain (str): The domain to search emails for.

        Returns:
            list[str]: A list of email addresses found under the specified domain.
        """
        return DomainSearcher(http_session=self._http_session).search_emails_by_domain(target_domain)

    def search_email_by_domain_and_name(self, target_domain: str, first_name: str, last_name: str) -> str | None:
        """
        Search for a specific email by domain and the person's name.

        Delegates the search for a specific email by domain and the person's name to the `DomainAndNameSearcher`.

        Args:
            target_domain (str): The domain to search the email in.
            first_name (str): The first name of the person.
            last_name (str): The last name of the person.

        Returns:
            str | None: The email address if found, otherwise None.
        """
        return DomainAndNameSearcher(http_session=self._http_session).search_email_by_domain_and_name(
            target_domain, first_name, last_name,
        )

    def check_if_email_is_valid(self, email: str) -> bool:
        """
        Verify the status of an email address.

        Delegates the verification of an email address to the `EmailVerifier`.

        Args:
            email (str): The email address to verify.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        return EmailVerifier(http_session=self._http_session).check_if_email_is_valid(email)

    def count_emails_by_domain(self, target_domain: str) -> int:
        """
        Count the number of emails associated with a given domain.

        Delegates the counting of emails associated with a given domain to the `EmailCounter`.

        Args:
            target_domain (str): The domain to count emails for.

        Returns:
            int: The total number of emails found for the given domain.
        """
        return EmailCounter(http_session=self._http_session).count_emails_by_domain(target_domain)
