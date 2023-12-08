"""A script demonstrating the interaction workflow with the Hunter.io API bindings provided by the library."""

from hunter_client.client import HunterClient
from hunter_client.exceptions import HunterError, InvalidInputError, TooManyRequestsError
from hunter_client.storages.dummy import DummyStorage

hunter_client = HunterClient(api_key='qwerty12345')
emails_storage = DummyStorage[str, list[str]]()

domains_to_search = ['example.com', 'anotherdomain.com', 'nonexistent.com']

for domain in domains_to_search:
    try:
        emails = hunter_client.search_emails_by_domain(domain)
    except InvalidInputError:
        print('Invalid input for domain: {0}'.format(domain))
    except TooManyRequestsError:
        print('Too many requests. Please try again later.')
    except HunterError:
        print('An unknown error occurred.')
    else:
        print('Emails found for {0}: {1}'.format(domain, emails))
        emails_storage.set(domain, emails)

    stored_emails = emails_storage.get(domain)
    if stored_emails:
        print('Stored emails for {0}: {1}'.format(domain, stored_emails))
    else:
        print('No emails stored for {0}'.format(domain))
