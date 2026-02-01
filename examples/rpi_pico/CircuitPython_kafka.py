import wifi
import socketpool
import ssl
import adafruit_requests
import os
import binascii
import json

SSID =  os.getenv('SSID')
PASSWORD = os.getenv('PASSWORD')
KAFKA_USER = os.getenv('KAFKA_USER')
KAFKA_PASS = os.getenv('KAFKA_PASS')
KAFKA_URL = os.getenv('KAFKA_URL')
class KafkaProducer:
    """Kafka Producer Class. Sends a simple message via Kafka Rest API.
    Requires SSID, PASSWORD, KAFKA_USER, KAFKA_PASS, KAFKA_URL
    """
    def __init__(self):
        self._connect = None
        self.session = None
        self.credentials = (
            binascii.b2a_base64(f"{KAFKA_USER}:{KAFKA_PASS}".encode()).decode().strip()
        )
        self.headers = {
            "Content-Type": "application/vnd.kafka.json.v2+json",
            "Authorization": f"Basic {self.credentials}"
        }
    def connect(self):
        if self.session:
            return
        wifi.radio.connect(SSID, PASSWORD)
        pool = socketpool.SocketPool(wifi.radio)
        ssl_context = ssl.create_default_context()
        self.session = adafruit_requests.Session(pool, ssl_context)
    def disconnect(self):
        if self.session:
            self.session = None
            wifi.radio.stop_station()

    @staticmethod
    def kafka_payload(msg) -> dict:
        return {"records":[{"value": {"value": msg}}]}

    def send(self, msg) -> int:
        """Send a simple message across to Kafka Broker based on REST URL.

        Args:
            msg (str): Message to send to Kafka. Supported types: [str, int, float, dict]

        Returns:
            int: Status code for returned message
        """
        if not isinstance(msg, (str, int, float, dict)):
            raise TypeError(f"Expected valid string instance, got {type(msg).__name__}")
        data = json.dumps(self.kafka_payload(msg))
        response = self.requests.post(KAFKA_URL, headers=self.headers, data=data)
        response.close()
        return response.status_code