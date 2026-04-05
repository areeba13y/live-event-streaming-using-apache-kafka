from kafka import KafkaConsumer
import json
from collections import defaultdict

consumer = KafkaConsumer(
    'traffic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

threshold = 500
ip_count = defaultdict(int)

for message in consumer:
    data = message.value
    ip = data["ip"]
    requests = data["requests"]

    ip_count[ip] += requests

    if ip_count[ip] > threshold:
        alert = {
            "ip": ip,
            "attack": "DDoS",
            "total_requests": ip_count[ip],
            "severity": "HIGH"
        }
        print("🚨 ALERT:", alert)

        # save to file
        with open("alerts.json", "a") as f:
            f.write(json.dumps(alert) + "\n")

        ip_count[ip] = 0