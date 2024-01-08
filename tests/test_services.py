import requests_mock

from hunter_client.services.email_validation import PersistentEmailValidationService
from hunter_client.storages.dummy import DummyStorage


def test_validate_and_store_valid_email(
    requests_mocker: requests_mock.Mocker,
    email_verification_successful_response: dict,
    persistent_email_validation_service: PersistentEmailValidationService,
    dummy_emails_validity_storage: DummyStorage[str, bool],
) -> None:
    requests_mocker.get(
        'https://api.hunter.io/v2/email-verifier?email=valid@example.com',
        json=email_verification_successful_response,
    )
    assert persistent_email_validation_service.validate_and_store_email_status('valid@example.com') is True
    assert dummy_emails_validity_storage.get('valid@example.com') is True


def test_validate_and_store_invalid_email(
    requests_mocker: requests_mock.Mocker,
    email_verification_failed_response: dict,
    persistent_email_validation_service: PersistentEmailValidationService,
    dummy_emails_validity_storage: DummyStorage[str, bool],
) -> None:
    requests_mocker.get(
        'https://api.hunter.io/v2/email-verifier?email=invalid@example.com',
        json=email_verification_failed_response,
    )
    assert persistent_email_validation_service.validate_and_store_email_status('invalid@example.com') is False
    assert dummy_emails_validity_storage.get('invalid@example.com') is False
