import os
from dotenv import load_dotenv
from kafka import KafkaConsumer, KafkaProducer, TopicPartition
from config import KafkaSettings
class KafkaConsumerBuilder:
    """Kafka Consumer Class Builder.

    Requires .build prior to runtime with settings class.
    """
    def __init__(self, settings: KafkaSettings):
        self.settings=  settings
        self.consumer = None
    def build(self, topic:str | None = 'building-events'):
        config = self.settings.model_dump()
        args = (topic, ) if topic else ()
        self.consumer = KafkaConsumer(*args, **config)
        return self.consumer
    def poll_values(self):
        if self.consumer is None:
            return Exception('Consumer not built. Please run .build()')
