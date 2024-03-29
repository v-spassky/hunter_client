import pytest


@pytest.fixture
def domain_search_successful_response() -> dict:
    return {
        'data': {
            'domain': 'example.com',
            'disposable': False,
            'webmail': False,
            'accept_all': False,
            'pattern': '{first}.{last}',
            'organization': 'Example Company',
            'description': 'Example Company is a company.',
            'industry': 'Information Technology',
            'twitter': None,
            'facebook': None,
            'linkedin': None,
            'instagram': None,
            'youtube': None,
            'technologies': [
                'amazon-web-services',
                'facebook',
                'intercom',
                'marketo',
                'node-js',
                'react',
                'recaptcha',
                'sentry',
            ],
            'country': None,
            'state': None,
            'city': None,
            'postal_code': None,
            'street': None,
            'emails': [
                {
                    'value': 'contact@example.com',
                    'type': 'personal',
                    'confidence': 95,
                    'sources': [
                        {
                            'domain': 'github.com',
                            'uri': 'http://github.com/ciaranlee',
                            'extracted_on': '2015-07-29',
                            'last_seen_on': '2017-07-01',
                            'still_on_page': True,
                        },
                    ],
                    'first_name': 'Contact',
                    'last_name': 'Person',
                    'position': 'Support',
                    'seniority': 'senior',
                    'department': 'customer_service',
                    'linkedin': None,
                    'twitter': None,
                    'phone_number': None,
                    'verification': {
                        'date': '2023-01-01',
                        'status': 'valid',
                    },
                },
                {
                    'value': 'info@example.com',
                    'type': 'personal',
                    'confidence': 90,
                    'sources': [
                        {
                            'domain': 'blog.intercom.io',
                            'uri': 'http://blog.intercom.io/were-hiring-a-support-engineer/',
                            'extracted_on': '2015-08-29',
                            'last_seen_on': '2017-07-01',
                            'still_on_page': True,
                        },
                    ],
                    'first_name': 'Info',
                    'last_name': 'Desk',
                    'position': 'Information',
                    'seniority': 'junior',
                    'department': 'general',
                    'linkedin': None,
                    'twitter': None,
                    'phone_number': None,
                    'verification': {
                        'date': '2023-01-02',
                        'status': 'valid',
                    },
                },
            ],
            'linked_domains': [],
        },
        'meta': {
            'results': 2,
            'limit': 10,
            'offset': 0,
            'params': {
                'domain': 'example.com',
                'company': None,
                'type': None,
                'seniority': None,
                'department': None,
            },
        },
    }


@pytest.fixture
def domain_and_name_search_successful_response() -> dict:
    return {
        'data': {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'score': 97,
            'domain': 'example.com',
            'accept_all': False,
            'position': 'Cofounder',
            'twitter': None,
            'linkedin_url': None,
            'phone_number': None,
            'company': 'Reddit',
            'sources': [
                {
                    'domain': 'redditblog.com',
                    'uri': 'http://redditblog.com/2008/10/22/some-post',
                    'extracted_on': '2018-10-19',
                    'last_seen_on': '2021-05-18',
                    'still_on_page': True,
                },
            ],
            'verification': {
                'date': '2021-06-14',
                'status': 'valid',
            },
        },
        'meta': {
            'params': {
                'first_name': 'John',
                'last_name': 'Doe',
                'full_name': None,
                'domain': 'example.com',
                'company': None,
                'max_duration': None,
            },
        },
    }


@pytest.fixture
def email_verification_successful_response() -> dict:
    return {
        'data': {
            'status': 'valid',
            'result': 'deliverable',
            'score': 100,
            'email': 'test@example.com',
            'regexp': True,
            'gibberish': False,
            'disposable': False,
            'webmail': False,
            'mx_records': True,
            'smtp_server': True,
            'smtp_check': True,
            'accept_all': False,
            'block': False,
            'sources': [
                {
                    'domain': 'exampledata.com',
                    'uri': 'http://exampledata.com/user-profile',
                    'extracted_on': '2023-01-01',
                    'last_seen_on': '2023-01-05',
                    'still_on_page': True,
                },
            ],
        },
        'meta': {
            'params': {
                'email': 'test@example.com',
            },
        },
    }


@pytest.fixture
def email_count_successful_response() -> dict:
    return {
        'data': {
            'total': 81,
            'personal_emails': 65,
            'generic_emails': 16,
            'department': {
                'executive': 10,
                'it': 0,
                'finance': 8,
                'management': 0,
                'sales': 0,
                'legal': 0,
                'support': 6,
                'hr': 0,
                'marketing': 0,
                'communication': 2,
                'education': 0,
                'design': 0,
                'health': 0,
                'operations': 0,
            },
            'seniority': {
                'junior': 13,
                'senior': 5,
                'executive': 2,
            },
        },
        'meta': {
            'params': {
                'domain': 'example.com',
                'company': None,
                'type': None,
            },
        },
    }
