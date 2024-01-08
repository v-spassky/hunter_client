import requests_mock

from hunter_client.client import HunterClient


def test_search_emails_by_domain(
    hunter_client: HunterClient,
    requests_mocker: requests_mock.Mocker,
    domain_search_successful_response: dict,
) -> None:
    requests_mocker.get(
        'https://api.hunter.io/v2/domain-search?domain=example.com',
        json=domain_search_successful_response,
    )

    response = hunter_client.domain_searcher.search_emails_by_domain('example.com')

    assert response == domain_search_successful_response


def test_search_email_by_domain_and_name(
    hunter_client: HunterClient,
    requests_mocker: requests_mock.Mocker,
    domain_and_name_search_successful_response: dict,
) -> None:
    requests_mocker.get(
        'https://api.hunter.io/v2/email-finder?domain=example.com&first_name=John&last_name=Doe',
        json=domain_and_name_search_successful_response,
    )

    response = hunter_client.domain_and_name_searcher.search_email_by_domain_and_name('example.com', 'John', 'Doe')

    assert response == domain_and_name_search_successful_response


def test_get_email_status(
    hunter_client: HunterClient,
    requests_mocker: requests_mock.Mocker,
    email_verification_successful_response: dict,
) -> None:
    requests_mocker.get(
        'https://api.hunter.io/v2/email-verifier?email=test@example.com',
        json=email_verification_successful_response,
    )

    response = hunter_client.email_verifier.check_if_email_is_valid('test@example.com')

    assert response == email_verification_successful_response


def test_count_emails_of_a_domain(
    hunter_client: HunterClient,
    requests_mocker: requests_mock.Mocker,
    email_count_successful_response: dict,
) -> None:
    requests_mocker.get(
        'https://api.hunter.io/v2/email-count?domain=example.com',
        json=email_count_successful_response,
    )

    response = hunter_client.email_counter.count_emails_by_domain('example.com')

    assert response == email_count_successful_response
