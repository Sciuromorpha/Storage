from sciuromorpha_storage.app import app, broker
from sciuromorpha_storage.mq_schema import storage_rpc, storage_topic
from faststream.rabbit.annotations import (
    Logger,
    Context,
    ContextRepo,
    RabbitBroker as BrokerAnnotation,
)


@app.on_startup
async def startup(
    logger: Logger,
):
    logger.debug("storage startup")


def get_template_file(self, meta_data: dict) -> dict:
    ## Depends on metadata, generate a template file for write/upload.
    return {}


def get_template_path(self, meta_data: dict) -> dict:
    ## Depends on metadata, generate a template folder for write/upload.
    return {}


def import_document(self, meta_data: dict) -> dict:
    # Import document from exiting file/folder etc.
    pass
