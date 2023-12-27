"""
This module defines the core models for the Hunter.io client.

Note that the model fields that represent relations to other models are late-initialized fields. This is because
there are use cases where the related models data is not immediately available at the time of model instantiation
from the context of an API response.

For example, when creating a `Email` model instance from a `/email-verifier` API response, there isn't any data
available to populate the `owner` field, so the field is left uninitialized.

It is the responsibility of the library to ensure that these fields are initialized before they are accessed. It is
okay to use a model instance with some fields being uninitialized if the use case doesn't require them to be
initialized (for example, we don't care about `Email.owner` if we're just checking whether the email is valid or not),
but accessing them before they are initialized will result in an exception.
"""

from hunter_client.constants import VALID_EMAIL_STATUS
from hunter_client.models.base import HunterModel
from hunter_client.models.lateinit import LateInitializedField


class Domain(HunterModel):
    """
    Represents a domain on the Internet.

    Note that `emails` being `Uninitialized` and `emails` being `[]` are two semantically different states.
    The former means that there could be related `Email` objects, but there wasn't any info about them when the
    `Domain` object was instantiated in a particular context. The latter means that there as a check for related
    `Email` objects and the result was that there are no related `Email` objects.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a `Domain` object.

        Args:
            name (str): The name of the domain.
        """
        self.name = name
        self.emails = LateInitializedField[list[Email]]()
        self.stats = LateInitializedField[DomainStats]()

    def add_email(self, email: 'Email') -> None:
        """
        Add an `Email` object to this `Domain`.

        Args:
            email (Email): The Email object to be added.
        """
        if email in self.emails.get():
            return
        self.emails.get().append(email)
        email.domain.set(self)

    def __repr__(self) -> str:
        """
        Provide a machine-readable representation of the `Domain` object.

        Returns:
            str: The representation of the Domain object.
        """
        return '<Domain(name={0})>'.format(self.name)

    def __str__(self) -> str:
        """
        Provide a human-readable representation of the `Domain` object.

        Returns:
            str: The name of the Domain.
        """
        return self.name


class Email(HunterModel):
    """Represents an email address."""

    def __init__(self, address: str, status: str) -> None:
        """
        Initialize an `Email` object.

        Args:
            address (str): The email address.
            status (str): The status of the email (e.g., `'valid'`, `'invalid'`).
        """
        self.address = address
        self.status = status
        self.owner = LateInitializedField[Person]()
        self.domain = LateInitializedField[Domain]()

    @property
    def is_valid(self) -> bool:
        """
        Check if the email is valid.

        Returns:
            bool: `True` if the email is valid, `False` otherwise.
        """
        return self.status == VALID_EMAIL_STATUS

    def __repr__(self) -> str:
        """
        Provide a machine-readable representation of the `Email` object.

        Returns:
            str: The representation of the `Email` object.
        """
        return '<Email(address={0})>'.format(self.address)

    def __str__(self) -> str:
        """
        Provide a human-readable representation of the `Email` object.

        Returns:
            str: The email address.
        """
        return self.address


class Person(HunterModel):
    """Represents a person. Typically in the context of being owner of an email address."""

    def __init__(self, first_name: str, last_name: str) -> None:
        """
        Initialize a `Person` object.

        Args:
            first_name (str): The first name of the person.
            last_name (str): The last name of the person.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = LateInitializedField[Email]()

    def __repr__(self) -> str:
        """
        Provide a machine-readable representation of the `Person` object.

        Returns:
            str: The representation of the `Person` object.
        """
        return '<Person(first_name={0}, last_name={1}>'.format(self.first_name, self.last_name)

    def __str__(self) -> str:
        """
        Provide a human-readable representation of the `Person` object.

        Returns:
            str: The full name of the `Person` instance.
        """
        return '{0} {1}'.format(self.first_name, self.last_name)


class DomainStats(HunterModel):
    """Represents statistical data associated with a domain."""

    def __init__(self, total_emails_count: int) -> None:
        """
        Initialize a `DomainStats` object.

        Args:
            total_emails_count (int): The total number of emails associated with the domain.
        """
        self.total_emails_count = total_emails_count
        self.domain = LateInitializedField[Domain]()

    def __repr__(self) -> str:
        """
        Provide a machine-readable representation of the `DomainStats` object.

        Returns:
            str: The representation of the `DomainStats` object.
        """
        return '<DomainStats(total_emails_count={0}, domain={1}>'.format(self.total_emails_count, self.domain)

    def __str__(self) -> str:
        """
        Provide a human-readable representation of the `DomainStats` object.

        Returns:
            str: A description of the domain and its total email count.
        """
        return '{0}: total_emails_count: {1}'.format(self.domain, self.total_emails_count)
