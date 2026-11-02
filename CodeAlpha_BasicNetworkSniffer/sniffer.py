
from datetime import datetime
import csv
import os

from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP

OUTPUT_FILE = "captured_packets.csv"
INTERFACE = "eth0"
HOST_FILTER = "host 10.42.168.71"
MAX_PACKETS = 50
CAPTURE_TIMEOUT = 30

captured_count = 0


def analyze_packet(packet):
    global captured_count
    captured_count += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    source = "N/A"
    destination = "N/A"
    protocol = "Other"

    if IP in packet:
        source = packet[IP].src
        destination = packet[IP].dst
    elif IPv6 in packet:
        source = packet[IPv6].src
        destination = packet[IPv6].dst

    if TCP in packet:
        protocol = "TCP"
    elif UDP in packet:
        protocol = "UDP"
    elif ICMP in packet:
        protocol = "ICMP"

    packet_length = len(packet)

    print(
        f"[{timestamp}] {protocol:<5} "
        f"{source} -> {destination} | "
        f"{packet_length} bytes"
    )

    file_exists = os.path.exists(OUTPUT_FILE)
    write_header = (
        not file_exists or os.path.getsize(OUTPUT_FILE) == 0
    )

    with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if write_header:
            writer.writerow([
                "Timestamp",
                "Protocol",
                "Source IP",
                "Destination IP",
                "Packet Length"
            ])

        writer.writerow([
            timestamp,
            protocol,
            source,
            destination,
            packet_length
        ])


def main():
    print("CodeAlpha - Basic Network Sniffer")
    print(f"Interface: {INTERFACE}")
    print(f"Filter: {HOST_FILTER}")
    print(f"Maximum packets: {MAX_PACKETS}")
    print(f"Timeout: {CAPTURE_TIMEOUT} seconds")
    print("Capturing authorized lab traffic only...\n")

    try:
        sniff(
            iface=INTERFACE,
            filter=HOST_FILTER,
            prn=analyze_packet,
            count=MAX_PACKETS,
            timeout=CAPTURE_TIMEOUT,
            store=False
        )

        print("\nCapture completed.")
        print(f"Total packets captured: {captured_count}")
        print(f"Results saved in: {OUTPUT_FILE}")

        if captured_count == 0:
            print("No packets captured. Check network traffic and filter.")

    except PermissionError:
        print("Permission denied. Run the script using sudo.")

    except OSError as error:
        print(f"Capture error: {error}")


if __name__ == "__main__":
    main()
