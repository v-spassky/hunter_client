"""This module provides an implementation of late-initialized fields for domain models in the Hunter.io client."""

from typing import Generic, TypeVar

from hunter_client.models.exceptions import UninitializedAttributeAccessError


class UninitializedType(object):
    """A class to represent uninitialized state."""

    def __repr__(self) -> str:
        """Provide a developer-oriented string representation of an uninitialized value."""
        return '<Uninitialized>'


Uninitialized = UninitializedType()
WrappedType = TypeVar('WrappedType')


class LateInitializedField(Generic[WrappedType]):
    """
    A generic class for defining late-initialized fields in models.

    This class allows the deferral of field initialization. It is useful in scenarios where certain model fields depend
    on resources or data that are not immediately available at the time of model instantiation.
    """

    def __init__(self) -> None:
        """Initialize a `LateInitializedField` instance with an uninitialized state."""
        self._inner_value: WrappedType | UninitializedType = Uninitialized

    def get(self) -> WrappedType:
        """
        Get the value of the late-initialized field.

        Returns:
            WrappedType: The value of the field if it has been initialized.

        Raises:
            UninitializedAttributeAccessError: If the field is accessed before it has been initialized.
        """
        if isinstance(self._inner_value, UninitializedType):
            raise UninitializedAttributeAccessError()
        return self._inner_value

    def set(self, new_value: WrappedType) -> None:
        """
        Set the value of the late-initialized field.

        Args:
            new_value (WrappedType): The value to set for the field.
        """
        self._inner_value = new_value
