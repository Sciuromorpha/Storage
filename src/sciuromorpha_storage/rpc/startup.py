from sciuromorpha_storage import S
from sciuromorpha_storage.app import app
from sciuromorpha_storage.settings import Settings, StorageConfig
from faststream.rabbit.annotations import (
    Logger,
    Context,
    ContextRepo,
    RabbitBroker as BrokerAnnotation,
)


@app.on_startup
async def startup(
    logger: Logger,
    settings: Settings = Context(),
    storage_config: StorageConfig = Context(),
):
    logger.debug("rpc startup begin.")
    from . import storage  # noqa: F401

    logger.debug("rpc startup end.")
