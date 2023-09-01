#!/usr/bin/python3

import sys
import requests

API_ENDPOINT = "https://www.nullroutenetworks.com/blocklist/submit.php"
API_KEY = "YOUR_API_KEY"

if len(sys.argv) < 2:
    print("Provide the IP to blacklist as the first command line argument.")
    exit()

# The host to blacklist
HOST = sys.argv[1]
# The time in seconds before expiry
EXPIRES = "86400"
# Trigger category ABUSE/HONEYPOT/etc
TYPE = "ABUSE"
# Trigger service SSH/HTTP/HTTPS/ASTERISK/etc
SERVICE = "SSH"

data = {'key':API_KEY,
        'host':HOST,
        'expires':EXPIRES,
        'type':TYPE,
        'service':SERVICE}

r = requests.post(url = API_ENDPOINT, data = data)

print(r.text)
