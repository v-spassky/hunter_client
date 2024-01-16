from typing import Generator

import pytest
import requests_mock

from hunter_client.client import HunterClient
from hunter_client.services.email_validation import PersistentEmailValidationService
from hunter_client.storages.dummy import DummyStorage
from tests.mock_responses.failed import *  # noqa: F401, F403, WPS347, WPS440
from tests.mock_responses.successful import *  # noqa: F401, F403, WPS347, WPS440


@pytest.fixture
def hunter_client() -> HunterClient:
    return HunterClient(api_key='not_really_an_api_key')


@pytest.fixture
def dummy_emails_by_domain_storage() -> DummyStorage[str, list[str]]:
    return DummyStorage[str, list[str]]()


@pytest.fixture
def dummy_emails_validity_storage() -> DummyStorage[str, bool]:
    return DummyStorage[str, bool]()


@pytest.fixture
def persistent_email_validation_service(
    dummy_emails_validity_storage: DummyStorage[str, bool],  # noqa: WPS442
) -> PersistentEmailValidationService:
    return PersistentEmailValidationService(
        hunter_api_key='not_really_an_api_key',
        results_storage=dummy_emails_validity_storage,
    )


@pytest.fixture
def requests_mocker() -> Generator[requests_mock.Mocker, None, None]:
    with requests_mock.Mocker() as mocker:
        yield mocker
