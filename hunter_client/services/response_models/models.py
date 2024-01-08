"""This module defines models that represent response body structures returned by the Hunter API."""

from pydantic import BaseModel

from hunter_client.services.response_models.data import (
    DomainAndNameSearcherResponseData,
    DomainSearcherResponseData,
    EmailCounterResponseData,
    EmailVerifierResponseData,
)
from hunter_client.services.response_models.meta import (
    DomainAndNameSearcherResponseMetaInfo,
    DomainSearcherResponseMetaInfo,
    EmailCounterResponseMetaInfo,
    EmailVerifierResponseMetaInfo,
)


class DomainSearcherResponse(BaseModel):
    """Represents the response from a `/domain-search` Hunter API endpoint."""

    data: DomainSearcherResponseData  # noqa: WPS110
    meta: DomainSearcherResponseMetaInfo


class DomainAndNameSearcherResponse(BaseModel):
    """Represents the response from the `/email-finder` Hunter API endpoint."""

    data: DomainAndNameSearcherResponseData  # noqa: WPS110
    meta: DomainAndNameSearcherResponseMetaInfo


class EmailVerifierResponse(BaseModel):
    """Represents the response from the `/email-verifier` Hunter API endpoint."""

    data: EmailVerifierResponseData  # noqa: WPS110
    meta: EmailVerifierResponseMetaInfo

    @property
    def is_valid(self) -> bool:
        """Return whether the email address is valid."""
        return self.data.status == 'valid'


class EmailCounterResponse(BaseModel):
    """Represents the response from the `/email-count` Hunter API endpoint."""

    data: EmailCounterResponseData  # noqa: WPS110
    meta: EmailCounterResponseMetaInfo
