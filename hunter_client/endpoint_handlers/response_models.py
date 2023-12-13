"""This module defines models that represent response body structures returned by the Hunter API."""

from pydantic import BaseModel, EmailStr, HttpUrl

from hunter_client.endpoint_handlers.response_models_components import (
    EmailCountsPerDepartmentData,
    EmailCountsPerSeniorityLevelData,
    EmailInfo,
    EmailVerificationInfo,
    InformationSource,
)


class DomainSearcherResponse(BaseModel):
    """Represents the response from a `/domain-search` Hunter API endpoint."""

    domain: str
    disposable: bool | None
    webmail: bool | None
    accept_all: bool | None
    pattern: str | None
    organization: str | None
    description: str | None
    industry: str | None
    twitter: str | None
    facebook: str | None
    linkedin: str | None
    instagram: str | None
    youtube: str | None
    technologies: list[str]
    country: str | None
    state: str | None
    city: str | None
    postal_code: str | None
    street: str | None
    emails: list[EmailInfo]
    linked_domains: list[str]

    @property
    def bare_emails(self) -> list[str]:
        """
        Extract just the email addresses from the detailed email information.

        Returns a list of email addresses as strings.
        """
        return [email.value for email in self.emails]


class DomainAndNameSearcherResponse(BaseModel):
    """Represents the response from the `/email-finder` Hunter API endpoint."""

    first_name: str | None
    last_name: str | None
    email: EmailStr | None
    score: int | None
    domain: str
    accept_all: bool | None
    position: str | None
    twitter: str | None
    linkedin_url: HttpUrl | None
    phone_number: str | None
    company: str | None
    sources: list[InformationSource]
    verification: EmailVerificationInfo


class EmailVerifierResponse(BaseModel):
    """Represents the response from the `/email-verifier` Hunter API endpoint."""

    status: str
    result: str | None  # noqa: WPS110
    score: int | None
    email: EmailStr
    regexp: bool | None
    gibberish: bool | None
    disposable: bool | None
    webmail: bool | None
    mx_records: bool | None
    smtp_server: bool | None
    smtp_check: bool | None
    accept_all: bool | None
    block: bool | None
    sources: list[InformationSource]

    @property
    def is_valid(self) -> bool:
        """Check if an email is considered valid according to the Hunter API response."""
        return self.status == 'valid'


class EmailCounterResponse(BaseModel):
    """Represents the response from the `/email-count` Hunter API endpoint."""

    total: int
    personal_emails: int
    generic_emails: int
    department: EmailCountsPerDepartmentData
    seniority: EmailCountsPerSeniorityLevelData
