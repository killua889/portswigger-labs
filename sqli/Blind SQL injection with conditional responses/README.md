# SQLi Tool

SQLi Tool is a Python-based script that helps retrieve an administrator's password through Blind SQL Injection using cookies. It performs a character-by-character brute-force attack to extract the password of the `administrator` user.

## Features
- Retrieve the administrator's password using Blind SQL Injection.
- Support for proxy (default: Burp Suite on `127.0.0.1:8080`).
- Option to use custom proxy settings or disable proxy.
- Command-line interface (CLI) for easy usage.
- Securely handle cookies during the attack.

## Prerequisites
To use this tool, you'll need:
- Python 3.x installed.
- `requests` library for making HTTP requests. You can install it using:
  ```bash
  pip install requests
## Arguments
- -u, --url: The target URL (e.g., https://www.example.com/).
- -t, --trackingid: The TrackingId cookie value.
- -s, --session: The session cookie value.
- -p, --proxy: Enable proxy usage (default: Burp Suite on 127.0.0.1:8080).

## How It Works
- The tool will brute-force the password of the administrator user by sending SQL injection payloads.
- For each attempt, it will check if the response contains the string "Welcome", indicating the correct character.
- It continues until the full password is retrieved.