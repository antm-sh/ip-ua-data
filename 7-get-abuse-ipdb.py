#!/usr/bin/env python3
import os
import requests
from datetime import datetime, timedelta


ABUSE_IPS_DIR = "abuse_ipdb"
OUTFILE = f"{ABUSE_IPS_DIR}/abuse-ips"

URL = "https://api.abuseipdb.com/api/v2/blacklist"
LIMIT = str(10000)

API_KEY = os.getenv('ABUSE_IPDB_API_KEY')
expiry_time = int((datetime.now() + timedelta(hours=4)).timestamp())

querystring = {
    'limit': LIMIT
}

headers = {
    'Accept': 'text/plain',
    'Key': API_KEY
}

os.makedirs(ABUSE_IPS_DIR, exist_ok=True)

response = requests.request(method='GET', url=URL, headers=headers, params=querystring)

with open(OUTFILE, 'w') as f:
    for line in response.text.splitlines():
        if line.strip() == "":
            continue
        f.write(f'{line}\n')


