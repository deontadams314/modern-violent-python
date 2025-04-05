# 🔐 Multi-Hash Password Cracker (Python + Passlib + Multiprocessing)

A lightweight, fast, and flexible password cracker built for CTFs, pentesting, and educational use. Supports cracking multiple hash types in parallel using a dictionary attack. Updated the violent python version.

## 🚀 Features

- ✅ Supports common hash formats:
  - `sha512_crypt` (`$6$`) — modern Linux shadow
  - `sha256_crypt` (`$5$`)
  - `md5_crypt` (`$1$`) — legacy Unix
  - `bcrypt` (`$2b$`) — web apps
  - `pbkdf2_sha256` — Django, Flask, etc.
- ✅ Accepts both `/etc/shadow`-style and raw hash-only input
- ✅ Uses multiprocessing for speed (tweakable `max_workers`)
- ✅ Shared dictionary in memory (no repeated file reads)
- ✅ Clean output of cracked results

---

## 📦 Setup

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

### 2. Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

###  3. Install Dependencies

```bash
pip install -r requirements.txt
```