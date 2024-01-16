"""This module defines models that represent the `meta` part of the response bodies returned by the Hunter API."""

from pydantic import BaseModel

from hunter_client.services.response_models.meta_params import (
    DomainAndNameSearcherResponseMetaInfoParams,
    DomainSearcherResponseMetaInfoParams,
    EmailCounterResponseMetaInfoParams,
    EmailVerifierResponseMetaInfoParams,
)


class DomainSearcherResponseMetaInfo(BaseModel):
    """Represents the `meta` part of a response from a `/domain-search` Hunter API endpoint."""

    results: int  # noqa: WPS110
    limit: int
    offset: int
    params: DomainSearcherResponseMetaInfoParams  # noqa: WPS110


class DomainAndNameSearcherResponseMetaInfo(BaseModel):
    """Represents the `meta` part of a response from the `/email-finder` Hunter API endpoint."""

    params: DomainAndNameSearcherResponseMetaInfoParams  # noqa: WPS110


class EmailVerifierResponseMetaInfo(BaseModel):
    """Represents the `meta` part of a response from the `/email-verifier` Hunter API endpoint."""

    params: EmailVerifierResponseMetaInfoParams  # noqa: WPS110


class EmailCounterResponseMetaInfo(BaseModel):
    """Represents the `meta` part of a response from the `/email-count` Hunter API endpoint."""

    params: EmailCounterResponseMetaInfoParams  # noqa: WPS110
