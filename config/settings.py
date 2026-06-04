from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from config.context import *


class Settings(BaseSettings):
    browserstack_user: str | None = None
    browserstack_key: str | None = None

    platform_name: str

    android_app: str | None = None

    device_name: str | None = None
    platform_version: str | None = None

    android_device: str | None = None
    android_os_version: str | None = None

    project_name: str | None = None
    build_name: str | None = None
    session_name: str | None = None

    app: str | None = None

    model_config = SettingsConfigDict(
        extra="ignore"
    )


settings = Settings()