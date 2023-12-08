"""
This module defines an abstract base class for results storage systems.

The ResultsStorage class in this module serves as a blueprint for creating various types of storage systems
that can store and manage key-value pairs. It employs generics for keys and values, allowing for flexible
implementation with different types. The keys are constrained to be hashable to ensure compatibility with
typical storage systems like dictionaries.

The class provides abstract methods that must be implemented by any concrete subclass: get, set, and delete.
These methods define the standard interface for interacting with the storage system.

Classes:
    ResultsStorage: An abstract base class for creating storage systems for key-value pairs.

Usage:
    This class is intended to be subclassed to create specific storage implementations. Implement the abstract
    methods get, set, and delete in the subclass to define the behavior of the storage system.
"""

from abc import ABC, abstractmethod
from typing import Generic, Hashable, TypeVar

Key = TypeVar('Key', bound=Hashable)
ValueToStore = TypeVar('ValueToStore')


class ResultsStorage(ABC, Generic[Key, ValueToStore]):
    """
    An abstract base class representing a generic storage for results.

    This class defines the basic interface for a results storage system, which includes methods to get, set,
    and delete values. It is designed to be subclassed to create concrete storage implementations.

    The storage uses a generic type for keys (which must be hashable) and values.

    Type Variables:
        Key: The type of the keys. Must be hashable.
        ValueToStore: The type of the values to store.

    Methods:
        get(key): Retrieves the value associated with the given key.
        set(key, value_to_store): Sets the value for a given key.
        delete(key): Removes the value associated with the given key.
    """

    @abstractmethod
    def get(self, key: Key) -> ValueToStore | None:
        """
        Retrieve the value associated with the specified key.

        Args:
            key (Key): The key for which to retrieve the value.

        Returns:
            ValueToStore | None: The value associated with the key, or None if the key does not exist.
        """
        pass  # noqa: WPS420

    @abstractmethod
    def set(self, key: Key, value_to_store: ValueToStore) -> None:
        """
        Set the value for the specified key.

        Args:
            key (Key): The key for which to set the value.
            value_to_store (ValueToStore): The value to store.
        """
        pass  # noqa: WPS420

    @abstractmethod
    def delete(self, key: Key) -> None:
        """
        Remove the value associated with the specified key.

        Args:
            key (Key): The key for which to remove the value.
        """
        pass  # noqa: WPS420
