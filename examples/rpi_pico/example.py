from CircuitPython_kafka import KafkaProducer
import random

kafka = KafkaProducer()
kafka.connect()

def simulate_chip_read() -> int:
    return random.randint(0,5)

currentuid = None
while True:
    uid = simulate_chip_read()
    if uid is not None:
        currentuid = uid
    if uid != currentuid:
        status = kafka.send(msg=str(uid))
        if status != 200:
            print(f'Error Sending: {status}') # You can choose whether you want to cleanly break/reset here
