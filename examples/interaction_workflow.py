"""A script demonstrating the interaction workflow with the Hunter.io API bindings provided by the library."""

import logging

from hunter_client.services.email_validation import PersistentEmailValidationService
from hunter_client.storages.dummy import DummyStorage

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

emails_storage = DummyStorage[str, bool]()
email_validation_service = PersistentEmailValidationService('qwerty12345', emails_storage)
emails_to_validate = ['email1@example.com', 'email2@anotherdomain.com', 'nonexistent@email.com']

for email in emails_to_validate:
    is_valid = email_validation_service.validate_and_store_email_status(email)

for stored_email in emails_to_validate:
    validity_check_result = emails_storage.get(stored_email)
    if not validity_check_result:
        logger.error('Somehow the email {0} was not stored in the storage system.'.format(stored_email))
    logger.info('Email {0} is valid: {1}'.format(stored_email, is_valid))
