"""This module provides an email validation service that integrates with the Hunter.io API."""

from hunter_client.client import HunterClient
from hunter_client.services.response_models import EmailVerifierResponse
from hunter_client.storages.interface import ResultsStorage


class PersistentEmailValidationService(object):
    """
    A service that validates email addresses using the Hunter.io API and stores the validation results.

    This service provides an interface to validate emails for their validity against the Hunter.io API and
    automatically persists the results using a specified storage mechanism. It is designed to facilitate
    applications where tracking and caching of email validation results are required.
    """

    def __init__(self, hunter_api_key: str, results_storage: ResultsStorage[str, bool]) -> None:
        """
        Initialize the email validation service.

        Args:
            hunter_api_key (str): The API key for accessing the Hunter.io API.
            results_storage (ResultsStorage[str, bool]): Storage system for saving validation results.
        """
        self._hunter_client = HunterClient(api_key=hunter_api_key)
        self._results_storage = results_storage

    def validate_and_store_email_status(self, email: str) -> bool:
        """
        Validate the given email and store the result.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: Whether the email address is valid or not.
        """
        email_verifier_raw_response = self._hunter_client.email_verifier.check_if_email_is_valid(email)
        email_verifier_response = EmailVerifierResponse.model_validate(email_verifier_raw_response)
        self._results_storage.set(email, email_verifier_response.is_valid)
        return email_verifier_response.is_valid
