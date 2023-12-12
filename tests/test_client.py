import requests_mock

from hunter_client.client import HunterClient


def test_search_emails_by_domain() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/domain-search?domain=example.com',
            json={
                'data': {
                    'emails': [
                        {'value': 'contact@example.com'},
                        {'value': 'info@example.com'},
                    ],
                },
            },
        )

        client = HunterClient(api_key='not_really_an_api_key')
        emails = client.search_emails_by_domain('example.com')

        assert emails == ['contact@example.com', 'info@example.com']


def test_search_email_by_domain_and_name() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/email-finder?domain=example.com&first_name=John&last_name=Doe',
            json={
                'data': {
                    'email': 'john.doe@example.com',
                },
            },
        )

        client = HunterClient(api_key='not_really_an_api_key')
        email = client.search_email_by_domain_and_name('example.com', 'John', 'Doe')

        assert email == 'john.doe@example.com'


def test_get_email_status() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/email-verifier?email=test@example.com',
            json={
                'data': {
                    'status': 'valid',
                },
            },
        )

        client = HunterClient(api_key='not_really_an_api_key')
        status = client.check_if_email_is_valid('test@example.com')

        assert status is True


def test_count_emails_of_domain() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/email-count?domain=example.com',
            json={
                'data': {
                    'total': 5,
                },
            },
        )

        client = HunterClient(api_key='not_really_an_api_key')
        count = client.count_emails_by_domain('example.com')

        assert count == 5
