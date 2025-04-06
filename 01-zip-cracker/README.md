![ZipCrack](assets/zipcrack.png)

# 🔐 ZipCrack — Multi-Process ZIP Password Cracker

**ZipCrack** is a high-performance, Python-based tool for cracking password-protected `.zip` files using a dictionary attack.  
It uses Python’s `concurrent.futures.ProcessPoolExecutor` to parallelize password attempts across all CPU cores.

---

## 🚀 Features

- ✅ CLI interface with argparse
- ✅ Multi-process cracking
- ✅ Gracefully stops after first successful crack
- ✅ Error-handling for corrupt zips, invalid passwords, and missing files
- ✅ Defaults to full CPU usage but customizable with `--workers`

---

## 📦 Usage

```bash
python main.py --zip {your-zip-here} --dict {your-wordlist-here}
```
### Arguements

  --zip       Path to password-protected .zip file  [REQUIRED]
  --dict      Path to dictionary file                [REQUIRED]
  --workers   Number of worker processes to use      [Default: CPU cores]

### 🛠 Example

```bash
python main.py --zip secret.zip --dict rockyou.txt --workers 4
```

Sample Output

``` bash
[*] Loaded 235886 passwords. Cracking with 4 workers...
[+] Password found: letmein123
```

---

## 📁 This is part of:

**Modern Violent Python**  
A Python 3+ repo focused on rebuilding classic offensive security tools using modern techniques.

> [← Back to main repo](../README.md)  
> [See all modernized tools](../.)
