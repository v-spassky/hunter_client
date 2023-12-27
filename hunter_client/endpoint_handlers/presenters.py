"""This module contains classes responsible for creating end-user presentation on model instances data."""

from hunter_client.models import Domain


class DomainPresenter(object):
    """Presenter class for `Domain` model instances."""

    def __init__(self, domain: Domain) -> None:
        """
        Initialize a `DomainPresenter` object.

        Args:
            domain (Domain): The `Domain` model instance to present.
        """
        self._domain = domain

    def bare_email_addresses(self) -> list[str]:
        """
        Return a list of bare email addresses associated with the domain.

        Returns:
            list[str]: A list of bare email addresses associated with the domain.
        """
        return [email.address for email in self._domain.emails.get()]
