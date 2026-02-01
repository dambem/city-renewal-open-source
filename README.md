
<div align="center">
  City Renewal Open Source Kafka
  <br />
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Authors & contributors](#authors--contributors)
- [License](#license)

</details>

---

## About

This is a small collection of snippets to effectively use a Pi Pico W, Kafka & FastAPI together.

### Built With
- Python FastAPI
- CircuitPython

## Getting Started

### Prerequisites

The examples found within rpi_pico require CircuitPython. 

### Installation

The usage snippets for rpi_pico can be drag & dropped into an appropriate CircuitPython directory. For CircuitPython, ensure you have a `settings.toml` with appropriate credentials.

At base, CircuitKafka will require the following:

```bash
SSID="X"
PASSWORD="X"
KAFKA_URL="X"
KAFKA_USER="X"
KAFKA_PASS="X"
```

## Usage


### CircuitPython & Pico W
```python
from CircuitPython_Kafka import KafkaProducer
kafka = KafkaProducer()
kafka.connect()
kafka.send('message')
kafka.send(123)
kafka.send({'a':'b'})
```

### FastAPI 
```

```


## Authors & contributors

The original setup of this repository is by [Damian Bemben](https://github.com/dambem).


## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.

