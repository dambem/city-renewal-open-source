from pydantic_settings import BaseSettings
from functools import lru_cache

class KafkaSettings(BaseSettings):
    bootstrap_servers: str
    client_id: str = "CONSUMER_CLIENT_ID"
    group_id: str = "CONSUMER_GROUP_ID"
    security_protocol: str = "SSL"
    api_version: tuple[int, int, int] = (2, 6, 0)
    ssl_cafile: str = "certs/ca.pem"
    ssl_certfile: str = "certs/service.cert"
    ssl_keyfile: str = "certs/service.key"


@lru_cache
def get_kafka_setting() -> KafkaSettings:
    return KafkaSettings()