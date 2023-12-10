from sciuromorpha_storage import S
from pydantic import (
    AliasChoices,
    AmqpDsn,
    Field,
    PostgresDsn,
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
    service_name: str = "storage"
    service_mode: str = Field(
        S.ENV_MODE_DEVELOPMENT, validation_alias=AliasChoices(S.ENV_CONFIG_MODE)
    )
    storage_config: str = Field(
        "./storage_conf.ini",
        validation_alias=AliasChoices(
            "storage_config", "storage_conf", "storage_config_file"
        ),
    )


import configparser
from typing import Union


class StorageConfig:
    config_files = ["./storage_conf.ini"]
    config = configparser.ConfigParser(allow_no_value=True, strict=True)

    def __init__(self, config_files: Union[list, str]) -> None:
        # Read Default Values
        self.config.read_dict(
            {
                "storage": {
                    "scope": ["host", "docker"],
                    "backend": ["fs", "cache"],
                },
                "fs": {"root": "./storage"},
                "cache": {"root": "./cache"},
                "docker": {"socket": "/var/run/docker.sock"},
            }
        )

        # Read init config file
        self.config.read(config_files)
