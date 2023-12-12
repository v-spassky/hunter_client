"""
This module defines the base types for handling different API endpoints of the Hunter service.

It provides a structured way to manage HTTP requests and responses, including error handling and URL formatting,
for interacting with the Hunter API. The module ensures a consistent approach for extending functionality
to various API endpoints and manages common tasks like error handling, session management, and URL construction.
"""


from abc import ABC, abstractmethod
from typing import NoReturn, NotRequired, TypedDict, Unpack
from urllib.parse import urlencode, urljoin

import requests

from hunter_client.exceptions import HunterError, HunterServerError, InvalidInputError, TooManyRequestsError


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

    def __init__(self, http_session: requests.Session) -> None:
        """
        Initialize an instance of the AbstractBaseEndpointHandler.

        Args:
            http_session (requests.Session): A session object used for making HTTP requests.
        """
        self._http_session = http_session

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
