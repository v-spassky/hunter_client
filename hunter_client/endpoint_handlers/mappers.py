"""Classes for responsible creating domain model instances from Hunter.io API responses."""

from hunter_client.constants import UNKNOWN_EMAIL_STATUS
from hunter_client.endpoint_handlers.response_models import (
    DomainAndNameSearcherResponse,
    DomainSearcherResponse,
    EmailCounterResponse,
    EmailVerifierResponse,
)
from hunter_client.models import Domain, DomainStats, Email, Person


class DomainMapper(object):
    """Mapper class for `Domain` objects."""

    @classmethod
    def from_domain_searcher_response(cls, dto: DomainSearcherResponse) -> Domain:
        """
        Create a `Domain` object from a `DomainSearcherResponse`.

        Args:
            dto (DomainSearcherResponse): Data transfer object containing information from the API response.

        Returns:
            Domain: A `Domain` model instance populated with data from the response.
        """
        domain = Domain(dto.data.domain)

        domain.emails.set([])
        for email_info in dto.data.emails:
            email_status = email_info.verification.status or UNKNOWN_EMAIL_STATUS
            email = Email(address=email_info.value, status=email_status)
            domain.add_email(email)

        return domain


class EmailMapper(object):
    """Mapper class for `Email` objects."""

    @classmethod
    def from_domain_and_name_searcher_response(cls, dto: DomainAndNameSearcherResponse) -> Email | None:
        """
        Create an `Email` object from a `DomainAndNameSearcherResponse`.

        Args:
            dto (DomainAndNameSearcherResponse): Data transfer object containing information from the API response.

        Returns:
            Email | None: An `Email` model instance if valid data is present in the response, otherwise, None.
        """
        if dto.data.first_name is None or dto.data.last_name is None:
            return None
        if dto.data.email is None:
            return None

        domain = Domain(name=dto.data.domain)
        owner = Person(first_name=dto.data.first_name, last_name=dto.data.last_name)
        email_status = dto.data.verification.status or UNKNOWN_EMAIL_STATUS
        email = Email(address=dto.data.email, status=email_status)

        domain.emails.set([])
        domain.add_email(email)
        email.owner.set(owner)
        owner.email.set(email)

        return email

    @classmethod
    def from_email_verifier_response(cls, dto: EmailVerifierResponse) -> Email:
        """
        Create an `Email` object from an `EmailVerifierResponse`.

        Args:
            dto (EmailVerifierResponse): Data transfer object containing information from the API response.

        Returns:
            Email: An `Email` model instance populated with data from the response.
        """
        return Email(address=dto.data.email, status=dto.data.status)


class DomainStatsMapper(object):
    """Mapper class for `DomainStats` objects."""

    @classmethod
    def from_email_counter_response(cls, dto: EmailCounterResponse) -> DomainStats:
        """
        Create a `DomainStats` object from an `EmailCounterResponse`.

        Args:
            dto (EmailCounterResponse): Data transfer object containing information from the API response.

        Returns:
            DomainStats: A `DomainStats` model instance populated with data from the response.
        """
        domain = Domain(dto.meta.params.domain)
        domain_stats = DomainStats(total_emails_count=dto.data.total)
        domain.stats.set(domain_stats)
        domain_stats.domain.set(domain)
        return domain_stats
