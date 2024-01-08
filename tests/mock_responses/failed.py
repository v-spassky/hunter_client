import pytest


@pytest.fixture
def domain_search_failed_response() -> dict:
    return {
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
    }


@pytest.fixture
def domain_and_name_search_failed_response() -> dict:
    return {
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
    }


@pytest.fixture
def email_verification_failed_response() -> dict:
    return {
        'data': {
            'status': 'invalid',
            'result': 'undeliverable',
            'score': 0,
            'email': 'invalid@example.com',
            'regexp': True,
            'gibberish': False,
            'disposable': False,
            'webmail': False,
            'mx_records': True,
            'smtp_server': True,
            'smtp_check': True,
            'accept_all': False,
            'block': False,
            'sources': [],
        },
        'meta': {
            'params': {
                'email': 'invalid@example.com',
            },
        },
    }


@pytest.fixture
def email_count_failed_response() -> dict:
    return {
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
    }
