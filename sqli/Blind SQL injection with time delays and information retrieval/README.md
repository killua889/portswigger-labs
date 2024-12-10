# SQL Injection Tool for Blind SQL injection with time delays and information retrieval

This tool automates blind SQL injection to solve the  Blind SQL injection with time delays and information retrieval lab in portswiger , specifically targeting cookies (e.g., TrackingId). It is designed for educational purposes to demonstrate SQL injection exploitation techniques.
## Features

    Exploits SQL injection vulnerabilities via cookies.
    Allows for proxy integration (e.g., Burp Suite).
    Retrieves sensitive information such as passwords from a database.
    Works with a custom character set (a-z0-9) for faster enumeration.

## Prerequisites

Before using the script, ensure you have the following installed:

    Python 3.x
    Required Python libraries:
        requests
        urllib3
        argparse

To install the libraries, use:

pip install requests urllib3

## How to Install

    Clone the repository:

    git clone https://github.com/killua889/portswigger-labs.git
    cd portswigger-labs/sqli/Blind\ SQL\ injection\ with\ time\ delays\ and\ information\ retrieval


    Verify the script file: Ensure main.py exists in the folder.

## Usage

Run the tool with the following command:
  ```bash

python main.py -u <url> -t <trackingid> -s <session> [-p]
-u : The target URL of the vulnerable application.
-t : The TrackingId cookie value.
-s : The session cookie value.
-p : Optional flag to use a proxy (default is Burp Suite on 127.0.0.1:8080).
  ```
Example:
  ```bash
python main.py -u "http://example.com" -t " your trackid " -s " your session " -p
  ```

Output Example
  ```bash
    Starting the attack:

[+] Target URL: https://target.com
[+] Using TrackingId value: TrackingId_value
[+] Using Session value: Session_value
[+] Proxy enabled. Requests will be routed through: http://127.0.0.1:8080

[+] Retrieving administrator password...
  ```