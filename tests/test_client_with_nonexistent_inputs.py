import requests_mock

from hunter_client.client import HunterClient


def test_search_emails_by_domain_no_result() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/domain-search?domain=nonexistent.com',
            json={
                'data': {
                    'domain': 'nonexistent.com',
                    'disposable': False,
                    'webmail': False,
                    'accept_all': False,
                    'pattern': None,
                    'organization': None,
                    'description': None,
                    'industry': None,
                    'twitter': None,
                    'facebook': None,
                    'linkedin': None,
                    'instagram': None,
                    'youtube': None,
                    'technologies': [],
                    'country': None,
                    'state': None,
                    'city': None,
                    'postal_code': None,
                    'street': None,
                    'emails': [],
                    'linked_domains': [],
                },
                'meta': {
                    'results': 0,
                    'limit': 10,
                    'offset': 0,
                    'params': {
                        'domain': 'nonexistent.com',
                        'company': None,
                        'type': None,
                        'seniority': None,
                        'department': None,
                    },
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
                    'first_name': 'John',
                    'last_name': 'Doe',
                    'email': None,
                    'score': 0,
                    'domain': 'nonexistent.com',
                    'accept_all': False,
                    'position': None,
                    'twitter': None,
                    'linkedin_url': None,
                    'phone_number': None,
                    'company': None,
                    'sources': [],
                    'verification': {
                        'date': None,
                        'status': None,
                    },
                },
                'meta': {
                    'params': {
                        'first_name': 'John',
                        'last_name': 'Doe',
                        'full_name': None,
                        'domain': 'nonexistent.com',
                        'company': None,
                        'max_duration': None,
                    },
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
                    'result': 'risky',
                    'score': 0,
                    'email': 'test@nonexistent.com',
                    'regexp': True,
                    'gibberish': False,
                    'disposable': False,
                    'webmail': False,
                    'mx_records': False,
                    'smtp_server': False,
                    'smtp_check': False,
                    'accept_all': True,
                    'block': False,
                    'sources': [],
                },
                'meta': {
                    'params': {
                        'email': 'test@nonexistent.com',
                    },
                },
            },
        )

        client = HunterClient(api_key='not_really_an_api_key')
        email_is_valid = client.check_if_email_is_valid('test@nonexistent.com')

        assert email_is_valid is False


def test_count_emails_of_a_nonexistent_domain() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/email-count?domain=nonexistent.com',
            json={
                'data': {
                    'total': 0,
                    'personal_emails': 0,
                    'generic_emails': 0,
                    'department': {
                        'executive': 0,
                        'it': 0,
                        'finance': 0,
                        'management': 0,
                        'sales': 0,
                        'legal': 0,
                        'support': 0,
                        'hr': 0,
                        'marketing': 0,
                        'communication': 0,
                        'education': 0,
                        'design': 0,
                        'health': 0,
                        'operations': 0,
                    },
                    'seniority': {
                        'junior': 0,
                        'senior': 0,
                        'executive': 0,
                    },
                },
                'meta': {
                    'params': {
                        'domain': 'nonexistent.com',
                        'company': None,
                        'type': None,
                    },
                },
            },
        )

        client = HunterClient(api_key='not_really_an_api_key')
        count = client.count_emails_by_domain('nonexistent.com')

        assert count == 0
