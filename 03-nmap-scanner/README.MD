# 🔎 Python Nmap Threaded Port Scanner

A using the `python-nmap` library for nmap scans in Python!  

---

## 🧠 Features

- 🔹 Threaded scanning using `ThreadPoolExecutor`
- 🔹 Supports `-sV` for service & version detection
- 🔹 Scan:
  - Individual ports (`--p 22,80`)
  - Port ranges (`--r 1-1000`)
- 🔹 Clean CLI with `argparse`
- 🔹 Optionally saves results to file with `--output`
- 🔹 Uses Python's `nmap.PortScanner` (requires Nmap installed)

---

## 📦 Requirements

- Python 3.6+
- `nmap` installed and in PATH
- `python-nmap` library

Install with:

```bash
pip install requirements.txt
```

---

## 🚀 Usage

```bash
python3 main.py --t <target> (--p <ports> | --r <range>) [--threads <num>] [--output <file>]
```

### Arguments:
| Flag | Description |
|------|-------------|
| `--t` | Target IP or hostname |
| `--p` | Comma-separated ports (e.g. `--p 22,80,443`) |
| `--r` | Port range (e.g. `--r 1-1024`) |
| `--threads` | Number of threads to scan in parallel (default: 100) |
| `--output` | Save results to a text file |

---

## 🧪 Examples

```bash
# Scan common ports with version detection
python3 main.py --t scanme.nmap.org --p 22,80

# Scan range of ports and save results
python3 main.py --t 192.168.1.1 --r 20-100 --output scan_results.txt

# Slow down scan to avoid detection
python3 main.py --t scanme.nmap.org --p 22,80 --threads 1
```

---

## 🛠 Sample Output

```
[+] Scan Results for [scanme.nmap.org] (45.33.32.156):
[*] Scanning ports: 22, 80
[*] scanme.nmap.org TCP/22 = open | Service: ssh OpenSSH 6.6.1p1
[*] scanme.nmap.org TCP/80 = open | Service: http Apache httpd 2.4.7
```

---

## ⚠️ Legal Warning

Use only on networks you **own** or have **explicit permission** to test. Unauthorized scanning is illegal and unethical.

---

> [← Back to main repo](../README.md)  
