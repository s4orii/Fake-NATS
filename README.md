# 🛰️ Fake NATS Server

`fake-nats.py` is a lightweight fake NATS server written in Python. It listens on the default NATS port and emulates a legitimate NATS server to capture client authentication attempts.

Perfect for **CTFs**, **red team simulations**, **reverse engineering**, or **honeypot setups**.

---

## ⚙️ Features

- Listens on `0.0.0.0:4222` (default NATS port)
- Sends a valid NATS `INFO` banner on connection
- Captures and prints incoming client payloads (e.g., credentials)
- Designed to reveal misconfigured or vulnerable NATS clients

---

## 🛠️ Requirements

- Python 3.x

---

## 🚀 Usage

```bash
python3 fake-nats.py
