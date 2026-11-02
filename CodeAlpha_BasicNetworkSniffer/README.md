# CodeAlpha – Basic Network Sniffer

A Python-based network packet capture and analysis tool built using **Scapy**. This project captures live network traffic, identifies basic protocol information, extracts source and destination IP addresses, and stores packet metadata in a CSV file for further analysis.

## 1. Project Overview

The Basic Network Sniffer is a cybersecurity project developed as part of the CodeAlpha Cyber Security Internship.

It monitors network traffic on a selected network interface and extracts useful packet information, including:

- Timestamp
- Source IP address
- Destination IP address
- Protocol type
- Packet length

Captured packet details are displayed in the terminal and saved in a CSV file.

## 2. Project Objectives

- Capture live network packets.
- Identify source and destination IP addresses.
- Detect common protocols such as TCP, UDP, and ICMP.
- Record packet timestamps and lengths.
- Apply packet capture filters.
- Export captured packet information into a CSV file.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Programming language |
| Scapy | Packet capture and analysis |
| Kali Linux | Testing environment |
| CSV | Store packet information |
| VirtualBox | Virtual machine environment |

## 4. Project Structure

```text
CodeAlpha_BasicNetworkSniffer/
│
├── sniffer.py
├── captured_packets.csv
├── README.md
├── requirements.txt
│
└── screenshots/
    ├── 01_Environment_Setup.png
    ├── 02_ICMP_Host_Filter_Tests.png
    ├── 03_Final_Sniffer_Execution.png
    └── 04_CSV_Output_Verification.png
```

## 5. Features

- Live packet capture using Scapy.
- IPv4 and IPv6 address extraction.
- TCP, UDP, and ICMP protocol identification.
- Timestamp recording.
- Packet length calculation.
- Host-based packet filtering.
- CSV export functionality.
- Configurable packet count and capture timeout.

## 6. Installation and Requirements

**Prerequisites:**
- Kali Linux or another compatible Linux environment.
- Python 3.
- Scapy.
- Appropriate permissions for packet capture.

Install Scapy:

```bash
sudo apt update
sudo apt install python3-scapy -y
```

Alternatively, install dependencies using:

```bash
pip install -r requirements.txt
```

## 7. Running the Project

Navigate to the project directory:

```bash
cd CodeAlpha_BasicNetworkSniffer
```

Run the sniffer with elevated permissions:

```bash
sudo python3 sniffer.py
```

The script captures traffic on the configured network interface (`eth0`) and applies the configured host filter.

**Configuration note:** The network interface and host IP filter should be updated according to the local network environment.

## 8. Testing and Results

The project was tested in Kali Linux using Scapy.

### Test 1 – Basic Packet Capture

Successfully captured live network packets through the `eth0` interface.

### Test 2 – ICMP Filter

Tested ICMP packet filtering by generating ping traffic to the network gateway.

**Result:** 4 ICMP packets captured successfully.

### Test 3 – Host-Based Filter

Tested a host-based BPF filter using the Kali Linux IP address (`10.42.168.71`).

**Result:** 4 matching packets captured successfully.

### Test 4 – Final Sniffer Execution

The final script execution successfully captured 12 packets.

| Packet Category | Count |
|---|---:|
| ICMP | 8 |
| Other | 4 |
| **Total** | **12** |

The captured packet information was successfully saved in `captured_packets.csv`.

*Note: These counts represent the final execution, not necessarily the total number of records in the CSV file.*

## 9. CSV Output

The captured packet metadata is stored in `captured_packets.csv`.

The CSV file contains:

- Timestamp
- Protocol
- Source IP
- Destination IP
- Packet Length

The script uses append mode (`a`) when writing to the CSV file. Therefore, new packet records are added to existing records rather than replacing them.

## 10. Limitations

- The current implementation identifies TCP, UDP, and ICMP protocols.
- Packets that do not match these protocol checks are classified as `Other`.
- Advanced payload inspection and deep packet analysis are not implemented.
- Packet capture depends on interface permissions and network configuration.

## 11. Learning Outcomes

Through this project, I gained practical experience in:

- Network packet capture using Scapy.
- Understanding IP addresses and common network protocols.
- Applying ICMP and host-based packet filters.
- Working with Python and Linux environments.
- Exporting packet metadata into CSV files.
- Performing basic network traffic analysis.

## 12. Disclaimer

This project was developed for educational purposes as part of a cybersecurity internship. Packet capture and monitoring should only be performed on networks for which proper authorization has been obtained.

---

**Project:** CodeAlpha – Basic Network Sniffer  
**Category:** Cybersecurity – Network Security  
**Programming Language:** Python  
**Packet Capture Library:** Scapy  
**Testing Environment:** Kali Linux
