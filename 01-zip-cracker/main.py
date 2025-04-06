#!/usr/bin/env python3

from concurrent.futures import ProcessPoolExecutor, as_completed
from zipfile import ZipFile, BadZipFile
import argparse
import zlib
import os

# Use the password input to open the .zip file
def try_password(zip_path, password):
    password = password.strip()
    
    try:
        with ZipFile(zip_path) as zf:
            zf.extractall(pwd=password.encode("utf-8"))
        return f"[+] Password found: {password}"
    except (RuntimeError, BadZipFile, zlib.error): 
        return None
    except Exception as e:
        return f"[!] Unexpected error: {e}"

# CLI Setup
def parse_args():
        parser = argparse.ArgumentParser(description="Multi-process .zip password cracker")
        parser.add_argument("--zip", required=True, help="Path to the .zip file")
        parser.add_argument("--dict", required=True, help="Path to the dictionary file")
        parser.add_argument("--workers", type=int, default=os.cpu_count(), help="Number of processes to use (default: CPU cores)")
        
        args = parser.parse_args()

        # Prompt if values are missing
        if not args.zip:
            args.zip = input("[?] Enter path to .zip file: ").strip()
        if not args.dict:
            args.dict = input("[?] Enter path to dictionary file: ").strip()
        
        return args

# Main function to run parellel process on the try_password function with a different password in each process
def main():
    args = parse_args()
    zip_path = args.zip
    dict_path = args.dict
    max_workers = args.workers

    if not os.path.isfile(zip_path):
        print(f"[!] Zip file not found: {zip_path}")
        return
    if not os.path.isfile(dict_path):
        print(f"[!] Dictionary file not found: {dict_path}")
        return

    with open(dict_path, 'r') as f:
        passwords = [line.strip() for line in f if line.strip()]

    print(f"[*] Loaded {len(passwords)} passwords. Cracking with {max_workers} workers...")

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(try_password, zip_path, pwd): pwd 
            for pwd in passwords
        }
        for future in as_completed(futures):
            result = future.result()
            if result:
                print(result)
                executor.shutdown(cancel_futures=True)
                return

    print("[-] Password not found in dictionary.")

if __name__ == "__main__":
    main()