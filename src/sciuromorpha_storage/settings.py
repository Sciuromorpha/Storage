import configparser
from typing import Union
from sciuromorpha_storage import S
from pydantic import (
    AliasChoices,
    AmqpDsn,
    Field,
    RedisDsn,
)
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="",
        extra="ignore",
        case_sensitive=False,
        str_strip_whitespace=True,
    )

    mq: AmqpDsn = Field(
        "amqp://guest:guest@localhost:5672/",
        validation_alias=AliasChoices(
            "mq", "rabbit", "rabbmitmq", "rabbitmq_url", "amqp"
        ),
    )
    redis: RedisDsn = Field(
        "redis://user:pass@localhost:6379/1",
        validation_alias=AliasChoices("redis", "redis_url"),
    )
    service_name: str = "storage"
    service_mode: str = Field(
        S.ENV_MODE_DEVELOPMENT, validation_alias=AliasChoices(S.ENV_CONFIG_MODE)
    )
    storage_config_file: list | str = Field(
        "./storage_conf.ini",
        validation_alias=AliasChoices(
            S.ENV_CONFIG_FILE, "storage_config", "storage_conf", "storage_config_file"
        ),
    )


class StorageConfig:
    config = configparser.ConfigParser(allow_no_value=True, strict=True)
    config_files = []

    def __init__(self, config_file: Union[list[str], str]) -> None:
        # Read Default Values
        self.config.read_dict(
            {
                S.CONFIG_SECTION_STORAGE: {
                    "scope": ["host", "docker"],
                    "backend": ["fs", "cache"],
                },
                S.CONFIG_SECTION_FS: {"root": "./storage"},
                S.CONFIG_SECTION_CACHE: {"root": "./cache"},
                S.CONFIG_SECTION_DOCKER: {"socket": "/var/run/docker.sock"},
            }
        )

        # Read init config file
        self.config_files = self.config.read(config_file)
