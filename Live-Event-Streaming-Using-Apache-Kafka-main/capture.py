from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime
import json

def save_log(log):
    try:
        with open("logs.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(log)

    with open("logs.json", "w") as f:
        json.dump(data, f, indent=4)

def label_event(port):
    labels = {
        22: "ssh_attempt",
        80: "web_request",
        443: "https_request",
        21: "ftp_attempt",
        3389: "rdp_attempt",
        23: "telnet_attempt",
    }
    return labels.get(port, "connection")

def process_packet(pkt):
    if IP not in pkt:
        return

    src_ip = pkt[IP].src
    dst_ip = pkt[IP].dst

    if TCP in pkt:
        protocol = "TCP"
        port = pkt[TCP].dport
    elif UDP in pkt:
        protocol = "UDP"
        port = pkt[UDP].dport
    else:
        protocol = "OTHER"
        port = None

    event = label_event(port) if port else "connection"

    log = {
        "timestamp": str(datetime.now()),
        "source_ip": src_ip,
        "destination_ip": dst_ip,
        "protocol": protocol,
        "port": port,
        "event": event
    }

    print(f"[LOG] {log['source_ip']} → port {port} | {event}")
    save_log(log)

print("[*] Starting capture for 60 seconds...")
sniff(prn=process_packet, store=0, timeout=60)
print("[*] Capture done. Logs saved to logs.json")

import subprocess
print("[*] Launching detection engine...")
subprocess.run(["python", "ddos_detector.py"])