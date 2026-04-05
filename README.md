# 🛡️ Live Event Streaming — DDoS Detection Using Apache Kafka

---

## 📌 Overview

A **real-time DDoS attack detection system** built with **Apache Kafka** and **Python**.  
The system simulates live network traffic, identifies abnormal high-traffic patterns,  
generates instant alerts, and visualizes everything on a **live dashboard**.

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| Apache Kafka | Real-time streaming pipeline |
| kafka-python | Kafka producer/consumer |
| Pandas | Data processing |
| Matplotlib | Visualization |
| Streamlit | Live dashboard |

---

## 📦 Installation
```bash
pip install kafka-python pandas matplotlib streamlit
```

---

## ▶️ How to Run

### ✅ Step 1 — Start Kafka Server
```bash
cd C:\kafka\kafka_2.13-4.2.0
bin\windows\kafka-server-start.bat config\server.properties
```
> ⚠️ Keep this terminal **open**

---

### ✅ Step 2 — Create Kafka Topic
```bash
cd C:\kafka\kafka_2.13-4.2.0
bin\windows\kafka-topics.bat --create --topic traffic \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```

---

### ✅ Step 3 — Run Producer (Traffic Generator)
```bash
python traffic_generator.py
```
> Simulates real-time network traffic

---

### ✅ Step 4 — Run Consumer (DDoS Detector)
```bash
python ddos_detector.py
```
> Detects DDoS attacks and prints live alerts

---

### ✅ Step 5 — Launch Dashboard
```bash
streamlit run dashboard_live.py
```
> Opens a live browser dashboard 🌐

---


## 📊 Sample Alert Output

Alerts are saved to `alerts.json`:
```json
{
  "ip": "192.168.1.5",
  "attack": "DDoS",
  "severity": "HIGH"
}
```

---

## ⚡ Features

- 🔴 Real-time network traffic simulation
- 🛡️ Automatic DDoS attack detection
- 📡 Kafka-based distributed streaming pipeline
- 📊 Live interactive dashboard via Streamlit
- 💾 Alert logging to JSON

---

