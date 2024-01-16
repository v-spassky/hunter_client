from hunter_client.storages.dummy import DummyStorage


def test_dummy_storage(dummy_emails_by_domain_storage: DummyStorage) -> None:
    assert dummy_emails_by_domain_storage.get('itch.io') is None

    dummy_emails_by_domain_storage.set('itch.io', ['ceo@itch.io', 'john@itch.io', 'paul@itch.io'])
    assert dummy_emails_by_domain_storage.get('itch.io') == ['ceo@itch.io', 'john@itch.io', 'paul@itch.io']

    dummy_emails_by_domain_storage.delete('itch.io')
    assert dummy_emails_by_domain_storage.get('itch.io') is None
