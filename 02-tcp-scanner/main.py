#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, as_completed
from socket import *
import argparse

# CLI Setup
def parse_args():
        parser = argparse.ArgumentParser(description="TCP Full Connect Port Scanner")
        parser.add_argument("--t", required=True, help="Target IP or Hostname")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--p", help="Target port(s), e.g. 22 or 21,22,80")
        group.add_argument("--r", help="Range of target ports, e.g. 1-443")
        parser.add_argument("--threads", type=int, default=100, help="Number of threads (default: 100)")
        parser.add_argument("--output", help="Optional output file to save results")
        
        args = parser.parse_args()

        if not args.t:
            args.t = input("[?] Enter target destination:  ").strip()
        
        return args

# Function to create socket to connect to target & tcp port
def portScan(target, port):
    try:
        con = socket(AF_INET, SOCK_STREAM)
        con.settimeout(2)
        con.connect((target, port))
        try:
            banner = con.recv(1024).decode().strip()
        except:
               banner = ""
        result = f"[+] {port}/TCP OPEN" + (f" | Banner: {banner}" if banner else "")
        con.close()
        return result
    except:
        print (f"[-] {port}/TCP CLOSED")
    
    return None

def main():
    results = []
    args = parse_args()
    target = args.t
    p_range = args.r

    # Turn port args into a list
    try:
        if args.p:
            ports = [int(p) for p in args.p.split(",")]
        elif args.r:
            start, end = [int(p.strip()) for p in args.r.split("-")]
            ports = list(range(start, end + 1))
    except ValueError:
            print("[-] Invalid port format.")
            return
    
    # Resolve hostname
    try:
        resolved_ip = gethostbyname(target)
    except:
        print(f"[-] Cannot resolve {target}: Unknown host")
        return

    print(f"[+] Scan Results for [{target}] ({resolved_ip}):")
    if args.r:
        print(f"[*] Scanning ports: {ports[0]} to {ports[-1]}")
    else:
        print(f"[*] Scanning ports: {', '.join(map(str, ports))}")

    # Run the scan
    try:
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            futures = [executor.submit(portScan, resolved_ip, port) for port in ports]
            for future in as_completed(futures):
                result = future.result()
                if result:
                    print(result)
                    results.append(result)
    except Exception as e:
        print(f"[!] Scan error: {e}")
        return

    # Output to file (only open ports)
    if args.output and results:
        try:
            with open(args.output, "w") as f:
                f.write("\n".join(results) + "\n")
            print(f"\n[+] Results saved to {args.output}")
        except Exception as e:
            print(f"[!] Could not write to {args.output}: {e}")

if __name__ == "__main__":
    main()
