"""This module defines models that represent nested parts of response body structures returned by the Hunter API."""

from datetime import date

from pydantic import BaseModel, EmailStr, HttpUrl


class InformationSource(BaseModel):
    """Represents a source of information about an email as it is declared in the Hunter API."""

    domain: str
    uri: HttpUrl
    extracted_on: date
    last_seen_on: date
    still_on_page: bool


class EmailVerificationInfo(BaseModel):
    """Represents verification information of an email as it is declared in the Hunter API."""

    date: date | None
    status: str | None


class EmailInfo(BaseModel):
    """Represents detailed information about an email address as it is declared in the Hunter API."""

    value: EmailStr  # noqa: WPS110
    type: str | None
    confidence: int | None
    sources: list[InformationSource]
    first_name: str | None
    last_name: str | None
    position: str | None
    seniority: str | None
    department: str | None
    linkedin: HttpUrl | None
    twitter: str | None
    phone_number: str | None
    verification: EmailVerificationInfo


class EmailCountsPerDepartmentData(BaseModel):
    """Represents aggregated data of email counts categorized by department within an organization."""

    executive: int
    it: int
    finance: int
    management: int
    sales: int
    legal: int
    support: int
    hr: int
    marketing: int
    communication: int
    education: int
    design: int
    health: int
    operations: int


class EmailCountsPerSeniorityLevelData(BaseModel):
    """Represents email counts categorized by seniority level in an organization."""

    junior: int
    senior: int
    executive: int
