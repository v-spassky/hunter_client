"""This module defines models that represent the `data` part of the response bodies returned by the Hunter API."""

from pydantic import BaseModel, EmailStr, HttpUrl

from hunter_client.services.response_models.components import (
    EmailCountsPerDepartmentData,
    EmailCountsPerSeniorityLevelData,
    EmailInfo,
    EmailVerificationInfo,
    InformationSource,
)


class DomainSearcherResponseData(BaseModel):
    """Represents the `data` part of a response from a `/domain-search` Hunter API endpoint."""

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


class DomainAndNameSearcherResponseData(BaseModel):
    """Represents the `data` part of a response from the `/email-finder` Hunter API endpoint."""

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


class EmailVerifierResponseData(BaseModel):
    """Represents the `data` part of a response from the `/email-verifier` Hunter API endpoint."""

    status: str
    result: str  # noqa: WPS110
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


class EmailCounterResponseData(BaseModel):
    """Represents the `data` part of a response from the `/email-count` Hunter API endpoint."""

    total: int
    personal_emails: int
    generic_emails: int
    department: EmailCountsPerDepartmentData
    seniority: EmailCountsPerSeniorityLevelData
