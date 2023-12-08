from hunter_client.storages.dummy import DummyStorage


def test_dummy_storage() -> None:
    domains_emails_storage = DummyStorage[str, list[str]]()
    assert domains_emails_storage.get('itch.io') is None

    domains_emails_storage.set('itch.io', ['ceo@itch.io', 'john@itch.io', 'paul@itch.io'])
    assert domains_emails_storage.get('itch.io') == ['ceo@itch.io', 'john@itch.io', 'paul@itch.io']

    domains_emails_storage.delete('itch.io')
    assert domains_emails_storage.get('itch.io') is None
