from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application Settings
    Store all non specific configurations
    Attributes:
        environment: indicates environment where runs the api (production, staging)
        sentry_url: URL for Sentry
    """

    environment: Optional[str]
    sentry_url: Optional[str]


settings = Settings()
