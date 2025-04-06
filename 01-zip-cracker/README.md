# 🔐 Zip Cracker — Multi-Process ZIP Password Cracker

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
