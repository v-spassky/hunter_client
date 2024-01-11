"""
This module defines the base types for handling different API endpoints of the Hunter service.

It provides a structured way to manage HTTP requests and responses, including error handling and URL formatting,
for interacting with the Hunter API. The module ensures a consistent approach for extending functionality
to various API endpoints and manages common tasks like error handling, session management, and URL construction.
"""

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, NotRequired, TypedDict, Unpack
from urllib.parse import urlencode, urljoin

import requests

if TYPE_CHECKING:
    from hunter_client.client import HunterClient

logger = logging.getLogger(__name__)


class PossibleQueryParams(TypedDict):
    """
    Typed dictionary to represent possible query parameters in an API request.

    This dictionary is used to specify and type-check the parameters that can be
    passed to the API endpoint.

    Attributes:
        domain (NotRequired[str]): An optional domain name to be included as a query parameter.
    """

    domain: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]


class AbstractBaseEndpointHandler(ABC):
    """
    Abstract base class for handling various API endpoints of the Hunter service.

    This class provides a common interface and utility methods for different endpoint
    handlers. It requires subclasses to define their own URL path and implements
    common functionalities like URL formatting and error dispatching.
    """

    _hunter_api_base_url = 'https://api.hunter.io'
    _current_api_version_path = '/v2'

    def __init__(self, client: 'HunterClient') -> None:
        """
        Initialize an instance of the AbstractBaseEndpointHandler.

        Args:
            client (HunterClient): An instance of the `HunterClient` class which is used to make HTTP requests.
        """
        self._client = client

    def before_request(self, method: str, url: str, **_query_params: Unpack[PossibleQueryParams]) -> None:
        """Request lifecycle hook before making an HTTP request."""
        logger.debug('Going to make an HTTP request: {0} {1}'.format(method, url))

    def after_request(self, response: requests.Response) -> None:
        """Request lifecycle hook after making an HTTP request."""
        logger.debug('Got HTTP response: {0} {1}'.format(response.status_code, response.url))

    def make_request(self, method: str, **query_params: Unpack[PossibleQueryParams]) -> requests.Response:
        """Central method to make HTTP requests."""
        url = self._formatted_url(**query_params)
        self.before_request(method, url, **query_params)
        response = self._client.http_session.request(method, url)
        self.after_request(response)
        response.raise_for_status()
        return response

    @property
    @abstractmethod
    def _endpoint_url_path(self) -> str:
        """
        An abstract property representing the URL path of the API endpoint.

        Subclasses must provide an implementation of this property, returning the specific
        path to their respective endpoint.

        Returns:
            str: The URL path for the API endpoint.
        """

    def _formatted_url(self, **query_params: Unpack[PossibleQueryParams]) -> str:
        """
        Format and return a full URL for making a request to the Hunter API.

        This method combines the base Hunter domain, the endpoint's specific URL path,
        and any provided query parameters into a complete URL.

        Args:
            query_params (Unpack[PossibleQueryParams]): A set of key-value pairs representing query parameters.

        Returns:
            str: The fully formatted URL.
        """
        joined_url = urljoin(self._hunter_api_base_url, self._current_api_version_path + self._endpoint_url_path)
        return '{0}?{1}'.format(joined_url, urlencode(query_params))
