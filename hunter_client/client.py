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

from typing import NoReturn

import requests

from hunter_client.exceptions import HunterError, HunterServerError, InvalidInputError, TooManyRequestsError


class HunterClient(object):
    """
    Client for interacting with the Hunter.io API via HTTP requests.

    This class exposes functionality of the Hunter.io API endpoints.
    See https://hunter.io/api-documentation/v2 for more information.
    """

    hunter_domain = 'https://api.hunter.io/v2'
    default_request_timeout = 5

    def __init__(
        self,
        api_key: str,
        request_timeout: int | None = None,
    ) -> None:
        """
        Initialize a new instance of the HunterClient class.

        Args:
            api_key (str): The API key for accessing the Hunter.io API.
            request_timeout (int | None, optional): The timeout in seconds for API requests, defaults to None.
        """
        self._api_key = api_key
        self._request_timeout = request_timeout or self.default_request_timeout

    def search_emails_by_domain(self, target_domain: str) -> list[str]:
        """
        Search for emails associated with a given domain.

        Args:
            target_domain (str): The domain to search emails for.

        Returns:
            list[str]: A list of email addresses found under the specified domain.
        """
        url = '{0}/domain-search?domain={1}&api_key={2}'.format(self.hunter_domain, target_domain, self._api_key)
        resp = requests.get(url, timeout=self._request_timeout)
        if resp.status_code != requests.codes.ok:
            self._dispatch_client_exception(resp)
        return [email['value'] for email in resp.json()['data']['emails']]

    def search_email_by_domain_and_name(self, target_domain: str, first_name: str, last_name: str) -> str | None:
        """
        Search for a specific email by domain and the person's name.

        Args:
            target_domain (str): The domain to search the email in.
            first_name (str): The first name of the person.
            last_name (str): The last name of the person.

        Returns:
            str | None: The email address if found, otherwise None.
        """
        url = '{0}/email-finder?domain={1}&first_name={2}&last_name={3}&api_key={4}'.format(
            self.hunter_domain, target_domain, first_name, last_name, self._api_key,
        )
        resp = requests.get(url, timeout=self._request_timeout)
        if resp.status_code != requests.codes.ok:
            self._dispatch_client_exception(resp)
        return resp.json()['data']['email']

    def check_if_email_is_valid(self, email: str) -> bool:
        """
        Verify the status of an email address.

        Args:
            email (str): The email address to verify.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        url = '{0}/email-verifier?email={1}&api_key={2}'.format(self.hunter_domain, email, self._api_key)
        resp = requests.get(url, timeout=self._request_timeout)
        if resp.status_code != requests.codes.ok:
            self._dispatch_client_exception(resp)
        return resp.json()['data']['status'] == 'valid'

    def count_emails_by_domain(self, target_domain: str) -> int:
        """
        Count the number of emails associated with a given domain.

        Args:
            target_domain (str): The domain to count emails for.

        Returns:
            int: The total number of emails found for the given domain.
        """
        url = '{0}/email-count?email={1}'.format(self.hunter_domain, target_domain)
        resp = requests.get(url, timeout=self._request_timeout)
        if resp.status_code != requests.codes.ok:
            self._dispatch_client_exception(resp)
        return resp.json()['data']['total']

    @classmethod
    def _dispatch_client_exception(cls, response: requests.Response) -> NoReturn:
        """
        Raise an appropriate exception based on the response status code.

        Args:
            response (requests.Response): The response to check.
        """
        exception: HunterError
        match response.status_code:
            case requests.codes.bad_request:
                exception = InvalidInputError()
            case requests.codes.too_many_requests:
                exception = TooManyRequestsError()
            case requests.codes.internal_server_error:
                exception = HunterServerError()
            case _:
                exception = HunterError()
        raise exception
