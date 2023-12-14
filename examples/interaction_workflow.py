"""A script demonstrating the interaction workflow with the Hunter.io API bindings provided by the library."""

import logging

from hunter_client.exceptions import HunterError, InvalidInputError, TooManyRequestsError
from hunter_client.services.email_validation import PersistentEmailValidationService
from hunter_client.storages.dummy import DummyStorage

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

emails_storage = DummyStorage[str, bool]()
email_validation_service = PersistentEmailValidationService('qwerty12345', emails_storage)
emails_to_validate = ['email1@example.com', 'email2@anotherdomain.com', 'nonexistent@email.com']

for email in emails_to_validate:
    try:
        is_valid = email_validation_service.validate_and_store_email_status(email)
    except InvalidInputError:
        logger.info('Invalid input for email: {0}'.format(email))
    except TooManyRequestsError:
        logger.error('Too many requests. Please try again later.')
    except HunterError:
        logger.error('An unknown error occurred.')
    else:
        logger.info('Email {0} validation result: {1}'.format(email, is_valid))
        stored_result = emails_storage.get(email)
        logger.info('Stored validation result for {0}: {1}'.format(email, stored_result))
