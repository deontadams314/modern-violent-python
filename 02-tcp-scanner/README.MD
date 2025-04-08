# ⚡ TCP Full Connect Port Scanner

A modern Python-based TCP port scanner with multithreaded scanning, optional banner grabbing, and support for saving results.

---

## 🔧 Features

- ✅ TCP 3-way handshake scan (not SYN stealth scan)
- ✅ Scan single ports, comma-separated lists, or full ranges
- ✅ Multi-threaded with configurable thread count
- ✅ Optional banner grabbing for open ports
- ✅ Output results to file using `--output`
- ✅ Domain name or raw IP support
- ✅ CLI-friendly interface

---

## 📦 Usage

```bash
python3 main.py --t <target> [--p <ports> | --r <range>] [--threads <num>] [--output <file>]
```

### Required:
- `--t` Target IP or domain name
- Either:
  - `--p` Comma-separated list of ports (e.g. `--p 22,80,443`)
  - `--r` Port range (e.g. `--r 1-1024`)

### Optional:
- `--threads` Number of scanning threads (default: 100)
- `--output` File to write scan results to

---

## 💡 Examples

Scan 3 common ports:

```bash
python3 main.py --t scanme.nmap.org --p 22,80,443
```

Scan full range with output saved:

```bash
python3 main.py --t 192.168.0.10 --r 1-1000 --output results.txt
```

---

## 🧪 Sample Output

```
[+] Scan Results for [scanme.nmap.org] (45.33.32.156):
[*] Scanning ports: 20 to 100
[-] 23/TCP CLOSED
[+] 22/TCP OPEN | Banner: SSH-2.0-OpenSSH_6.6.1p1
[+] 80/TCP OPEN
[+] Results saved to results.txt
```

---

## ⚠️ Legal Notice

This tool is for **educational and authorized testing only**. Do **not** use against systems or networks you do not own or have permission to scan.

---

> [← Back to main repo](../README.md)  
