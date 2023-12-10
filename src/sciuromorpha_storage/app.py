import os
from uuid import uuid4
from faststream import FastStream, Context
from faststream.rabbit import RabbitBroker
from faststream.rabbit.annotations import (
    Logger,
    ContextRepo,
    RabbitBroker as BrokerAnnotation,
)

from sciuromorpha_storage import S, Settings
from sciuromorpha_storage.mq_schema import service_status

broker = RabbitBroker()
app = FastStream(broker)


@app.on_startup
async def setup(context: ContextRepo, logger: Logger, env: str = ".env"):
    service_id = str(uuid4())
    context.set_global("service_id", service_id)

    settings = Settings(_env_file=os.environ.get(S.ENV_DOT_FILE, env))
    context.set_global("settings", settings)

    await broker.connect(str(settings.mq))
    logger.debug("connect to mq success")


@app.after_startup
async def publish_online(
    logger: Logger,
    broker: BrokerAnnotation,
    service_id: str = Context(),
    settings: Settings = Context(),
):
    # Publish online message to broker.
    await broker.publish(
        {
            "service": settings.service_name,
            "status": S.SERVICE_STATUS_ONLINE,
            "service_id": service_id,
        },
        routing_key="service.storage",
        exchange=service_status,
    )
    logger.info("Storage service startup success.")


@app.on_shutdown
async def publish_offline(
    logger: Logger,
    broker: BrokerAnnotation,
    service_id: str = Context(),
    settings: Settings = Context(),
):
    # Publish online message to broker.
    await broker.publish(
        {
            "service": settings.service_name,
            "status": S.SERVICE_STATUS_OFFLINE,
            "service_id": service_id,
        },
        routing_key="service.storage",
        exchange=service_status,
    )
    logger.info("Storage service shutdown success.")
