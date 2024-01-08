"""This module defines models that represent the `params` part of the models defined in `meta.py`."""

from pydantic import BaseModel, EmailStr


class DomainSearcherResponseMetaInfoParams(BaseModel):
    """Represents the `meta.params` part of a response from a `/domain-search` Hunter API endpoint."""

    domain: str
    company: str | None
    type: str | None
    seniority: str | None
    department: str | None


class DomainAndNameSearcherResponseMetaInfoParams(BaseModel):
    """Represents the `meta.params` part of a response from the `/email-finder` Hunter API endpoint."""

    first_name: str
    last_name: str
    full_name: str | None
    domain: str
    company: str | None
    max_duration: int | None


class EmailVerifierResponseMetaInfoParams(BaseModel):
    """Represents the `meta.params` part of a response from the `/email-verifier` Hunter API endpoint."""

    email: EmailStr


class EmailCounterResponseMetaInfoParams(BaseModel):
    """Represents the `meta.params` part of a response from the `/email-count` Hunter API endpoint."""

    domain: str
    company: str | None
    type: str | None
