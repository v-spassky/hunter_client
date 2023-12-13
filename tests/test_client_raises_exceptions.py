import pytest
import requests
import requests_mock

from hunter_client.client import HunterClient
from hunter_client.exceptions import HunterError, HunterServerError, InvalidInputError, TooManyRequestsError


def test_dispatch_invalid_input_exception() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/domain-search?domain=invalid_domain',
            status_code=requests.codes.bad_request,
        )
        client = HunterClient(api_key='not_really_an_api_key')
        with pytest.raises(InvalidInputError):
            client.search_emails_by_domain('invalid_domain')


def test_dispatch_too_many_requests_exception() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/domain-search?domain=example.com',
            status_code=requests.codes.too_many_requests,
        )
        client = HunterClient(api_key='not_really_an_api_key')
        with pytest.raises(TooManyRequestsError):
            client.search_emails_by_domain('example.com')


def test_dispatch_server_error_exception() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/domain-search?domain=example.com',
            status_code=requests.codes.internal_server_error,
        )
        client = HunterClient(api_key='not_really_an_api_key')
        with pytest.raises(HunterServerError):
            client.search_emails_by_domain('example.com')


def test_dispatch_generic_client_error_exception() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/domain-search?domain=example.com',
            status_code=requests.codes.im_a_teapot,
        )
        client = HunterClient(api_key='not_really_an_api_key')
        with pytest.raises(HunterError):
            client.search_emails_by_domain('example.com')
