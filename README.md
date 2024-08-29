# crack-db-drill
crack tool

This tool is brute-force to mysql DB.

If no options are given, the default files in the sample directory are used.

## Usage
```bash
git clone https://github.com/cybertramp/crack-db-drill.git
cd crack-db-drill
poetry shell
poetry install
python crack.py
```

## Options
```bash
usage: crack.py [-h] [-i IP_FILE] [-u USER_FILE] [-w PW_FILE] [-p PORT] [-t THREADS]

MySQL Password Recovery Script

options:
  -h, --help            show this help message and exit
  -i IP_FILE, --ip_file IP_FILE
                        File containing IP addresses
  -u USER_FILE, --user_file USER_FILE
                        File containing usernames
  -w PW_FILE, --pw_file PW_FILE
                        File containing passwords
  -p PORT, --port PORT  MySQL port number
  -t THREADS, --threads THREADS
                        Number of threads
```

---

This tool is not recommended for malicious purposes.

### Ref
- Password samples: [SecLists](https://github.com/danielmiessler/SecLists)

---