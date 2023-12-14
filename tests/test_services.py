import requests_mock

from hunter_client.services.email_validation import PersistentEmailValidationService
from hunter_client.storages.dummy import DummyStorage


def test_validate_and_store_valid_email() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/email-verifier?email=valid@example.com',
            json={
                'data': {
                    'status': 'valid',
                    'result': 'deliverable',
                    'score': 100,
                    'email': 'valid@example.com',
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
                        'email': 'valid@example.com',
                    },
                },
            },
        )
        results_storage = DummyStorage[str, bool]()
        email_validation_service = PersistentEmailValidationService('fake_api_key', results_storage)
        assert email_validation_service.validate_and_store_email_status('valid@example.com') is True
        assert results_storage.get('valid@example.com') is True


def test_validate_and_store_invalid_email() -> None:
    with requests_mock.Mocker() as mocker:
        mocker.get(
            'https://api.hunter.io/v2/email-verifier?email=invalid@example.com',
            json={
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
            },
        )
        results_storage = DummyStorage[str, bool]()
        email_validation_service = PersistentEmailValidationService('fake_api_key', results_storage)
        assert email_validation_service.validate_and_store_email_status('invalid@example.com') is False
        assert results_storage.get('invalid@example.com') is False
