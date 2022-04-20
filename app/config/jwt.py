from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """JWT Settings

    Attributes:
        environment: indicates environment where runs the api (production, staging)
        sentry_url: URL for Sentry
    """

    secret_key: Optional[
        str
    ] = "9a2d3db2988f11f6cc7659167e193c045885d013c6f46b0ca09af0f9f210a6cc"
    algorithm: Optional[str] = "HS256"
    access_token_expire_minutes: Optional[int] = 30


settings = Settings()
