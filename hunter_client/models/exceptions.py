"""This module defines exceptions that represent invalid states of model instances."""

from hunter_client.models.base import HunterModelError


class UninitializedAttributeAccessError(HunterModelError):
    """Raised when a late-initialized uninitialized attribute is accessed before it is initialized."""

    def __repr__(self) -> str:
        """Provide a developer-oriented string representation of the error."""
        return '<UninitializedAttributeAccessError>'

    def __str__(self) -> str:
        """Provide a human-readable string representation of the error."""
        return 'An uninitialized attribute of a model instance was accessed before it was initialized.'
