import requests_mock

from hunter_client.client import HunterClient


def test_search_emails_by_domain_no_result(
    hunter_client: HunterClient,
    requests_mocker: requests_mock.Mocker,
    doamin_search_failed_response: dict,
) -> None:
    requests_mocker.get(
        'https://api.hunter.io/v2/domain-search?domain=nonexistent.com',
        json=doamin_search_failed_response,
    )

    emails = hunter_client.domain_searcher.search_emails_by_domain('nonexistent.com')

    assert emails == []  # noqa: WPS520


def test_search_email_by_random_domain_and_name(
    hunter_client: HunterClient,
    requests_mocker: requests_mock.Mocker,
    domain_and_name_search_failed_response: dict,
) -> None:
    requests_mocker.get(
        'https://api.hunter.io/v2/email-finder?domain=nonexistent.com&first_name=John&last_name=Doe',
        json=domain_and_name_search_failed_response,
    )

    email = hunter_client.domain_and_name_searcher.search_email_by_domain_and_name('nonexistent.com', 'John', 'Doe')

    assert email is None


def test_get_invalid_email_status(
    hunter_client: HunterClient,
    requests_mocker: requests_mock.Mocker,
    email_verification_failed_response: dict,
) -> None:
    requests_mocker.get(
        'https://api.hunter.io/v2/email-verifier?email=invalid@example.com',
        json=email_verification_failed_response,
    )

    email_is_valid = hunter_client.email_verifier.check_if_email_is_valid('invalid@example.com')

    assert email_is_valid is False


def test_count_emails_of_a_nonexistent_domain(
    hunter_client: HunterClient,
    requests_mocker: requests_mock.Mocker,
    email_count_failed_response: dict,
) -> None:
    requests_mocker.get(
        'https://api.hunter.io/v2/email-count?domain=nonexistent.com',
        json=email_count_failed_response,
    )

    count = hunter_client.email_counter.count_emails_by_domain('nonexistent.com')

    assert count == 0
