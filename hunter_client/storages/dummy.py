"""
This module provides a simple implementation of the ResultsStorage interface for testing or development purposes.

The DummyStorage class defined here is a basic in-memory storage system that mimics a key-value store. It's a
concrete implementation of the ResultsStorage abstract base class, utilizing a standard Python dictionary for
storing data. This class can be used for development or testing where a simple and transient storage mechanism
is required.

Classes:
    DummyStorage: A simple in-memory storage system for key-value pairs.

Usage:
    Instantiate the DummyStorage class and use its get, set, and delete methods to interact with the in-memory
    key-value store. It can serve as a stand-in for more complex storage systems during development or testing.
"""

from typing import Generic

from hunter_client.storages.interface import Key, ResultsStorage, ValueToStore


class DummyStorage(ResultsStorage, Generic[Key, ValueToStore]):
    """
    A simple in-memory implementation of the ResultsStorage interface.

    This class provides a basic in-memory key-value store. It's useful for testing or development scenarios
    where a simple and non-persistent storage is sufficient.

    Type Variables:
        Key: The type of the keys used in the storage. Must be hashable.
        ValueToStore: The type of the values to be stored.

    Attributes:
        _repository (dict[Key, ValueToStore]): The underlying dictionary used for storage.
    """

    def __init__(self) -> None:
        """Initialize the `DummyStorage` with an empty repository."""
        self._repository: dict[Key, ValueToStore] = {}

    def get(self, key: Key) -> ValueToStore | None:
        """
        Retrieve the value associated with the specified key.

        Args:
            key (Key): The key for which to retrieve the value.

        Returns:
            ValueToStore | None: The value associated with the key, or None if the key does not exist.
        """
        return self._repository.get(key)

    def set(self, key: Key, value_to_store: ValueToStore) -> None:
        """
        Set the value for the specified key.

        Args:
            key (Key): The key for which to set the value.
            value_to_store (ValueToStore): The value to store.
        """
        self._repository[key] = value_to_store

    def delete(self, key: Key) -> None:
        """
        Remove the value associated with the specified key.

        Args:
            key (Key): The key for which to remove the value.
        """
        self._repository.pop(key, None)
