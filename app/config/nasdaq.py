from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """NASDAQ Settings

    Attributes:
        nasdaq_url: URL for Sentry
    """

    nasdaq_url: Optional[str]


settings = Settings()
