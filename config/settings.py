from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
from pydantic import Field
from config.context import *


class Settings(BaseSettings):
    browserstack_user: str | None = Field(default=None, alias="browserstack_user")
    browserstack_key: str | None = Field(default=None, alias="browserstack_key")

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