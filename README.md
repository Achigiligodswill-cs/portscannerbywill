# 🔍 Python Port Scanner

A simple TCP port scanner built with Python. It scans a host for open ports in a specified range and attempts to grab service banners if available.

## 🚀 Features

- Scans a single host using TCP connections
- Allows custom port ranges
- Detects open and closed ports
- Grabs banners for basic service identification
- Measures scan duration

## 🛠 Requirements

- Python 3.x  
(No external libraries required)

## 💻 How to Use

Run the script using Python:

```bash
python3 port_scanner.py
Enter a host to scan: localhost
localhost
127.0.0.1
Scanning (127.0.0.1)

Checking port 8080
Port 8080 result: 0
Port 8080 is OPEN
Banner: HTTP/1.0 200 OK
...

Scan completed in: 0:00:01.001234
