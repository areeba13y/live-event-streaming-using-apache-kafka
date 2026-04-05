import json
from collections import defaultdict

print("[*] Detection engine started...")

try:
    with open("logs.json", "r") as f:
        logs = json.load(f)
except:
    print("[!] logs.json not found!")
    logs = []

ip_count = defaultdict(int)
threshold = 5

for log in logs:
    ip = log.get("source_ip", "unknown")
    ip_count[ip] += 1

for ip, count in ip_count.items():
    if count > threshold:
        alert = {
            "ip": ip,
            "count": count,
            "status": "ATTACK",
            "severity": "HIGH"
        }
    else:
        alert = {
            "ip": ip,
            "count": count,
            "status": "Normal",
            "severity": "LOW"
        }

    print(f"[INFO] {ip} → {count} requests | {alert['status']}")

    with open("alerts.json", "a") as f:
        f.write(json.dumps(alert) + "\n")

print("[*] Detection done! alerts.json updated.")