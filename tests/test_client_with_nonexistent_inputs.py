import requests_mock

from hunter_client.client import HunterClient


def test_search_emails_by_domain_no_result() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/domain-search?domain=nonexistent.com',
            json={
                'data': {
                    'emails': [],
                },
            },
        )

        client = HunterClient(api_key='not_really_an_api_key')
        emails = client.search_emails_by_domain('nonexistent.com')

        assert emails == []  # noqa: WPS520


def test_search_email_by_random_domain_and_name() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/email-finder?domain=nonexistent.com&first_name=John&last_name=Doe',
            json={
                'data': {
                    'email': None,
                },
            },
        )

        client = HunterClient(api_key='not_really_an_api_key')
        email = client.search_email_by_domain_and_name('nonexistent.com', 'John', 'Doe')

        assert email is None


def test_get_invalid_email_status() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/email-verifier?email=test@nonexistent.com',
            json={
                'data': {
                    'status': 'accept_all',
                },
            },
        )

        client = HunterClient(api_key='not_really_an_api_key')
        email_is_valid = client.check_if_email_is_valid('test@nonexistent.com')

        assert email_is_valid is False


def test_count_emails_of_noneistent_domain() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/email-count?domain=nonexistent.com',
            json={
                'data': {
                    'total': 0,
                },
            },
        )

        client = HunterClient(api_key='not_really_an_api_key')
        count = client.count_emails_by_domain('nonexistent.com')

        assert count == 0
