#!/usr/bin/env python3

from passlib.context import CryptContext
from concurrent.futures import ProcessPoolExecutor
import os

# Supported hash types
pwd_context = CryptContext(schemes=[
    "sha512_crypt", # /etc/shadow (modern Linux)
    "sha256_crypt", # common
    "md5_crypt",  #  legacy unix
    "bcrypt", # common web apps
    "pbkdf2_sha256" # Django, Flask, etc.
    ])

# Shared wordlist
dictWords = []

# Input files
dict_file = "dictionary.txt"
password_file = "passwords.txt"

# Shared dictionary init
def init_dict(words):
    global dictWords
    dictWords = words

# Cracking logic per user/hash
def testPass(user, cryptPass):
    try:
        for word in dictWords:
                try:
                    if pwd_context.verify(word, cryptPass):
                        hash_type = pwd_context.identify(cryptPass)
                        return f"[+] Found Password For {user}: {word}  [Hash type: {hash_type}]\n"
                except Exception:
                        continue
        return f"[-] Password Not Found for {user}"
    except Exception as e:
        return f"[!] Error for {user}: {e}"


def main():
    tasks = []

    if not os.path.exists(dict_file) or not os.path.exists(password_file):
        print("[!] Make sure dictionary.txt and passwords.txt exist in the same folder.")
        return
    
    # Load dictionary
    with open(dict_file, 'r') as f:
        words = [w.strip() for w in f if w.strip()]
    
# Load hashes (shadow-style or raw)
    with open(password_file, 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue

            if ":" in line:
                user = line.split(':')[0]
                crypt_pass = line.split(':')[1].strip()
            else:
                user = f"hash_{i}"
                crypt_pass = line

            tasks.append((user, crypt_pass))
    
    # Multi-thread cracking
    with ProcessPoolExecutor(max_workers=4, initializer=init_dict, initargs=(words,)) as executor:
        futures = [executor.submit(testPass, user, crypt_pass) for user, crypt_pass in tasks]
        for future in futures:
            result = future.result()
            if result:
                print(result)
            

if __name__ == "__main__":
    main()