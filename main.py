import time
import subprocess
import requests
import json

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USERKEY = os.getenv('USERKEY')
PASSKEY = os.getenv('PASSKEY')

def send(to, msg):
    url = "https://reguler.zenziva.net/apps/smsapi.php?userkey=" + USERKEY + "&passkey=" + PASSKEY + "&nohp=" + to + "&pesan=" + msg
    r = requests.get(url)
    print(r.text)

print("Zenziva sender started...")

# waiting & read from notifications file
f = subprocess.Popen(['tail','-f','notifications'], \
    stdout=subprocess.PIPE,stderr=subprocess.PIPE)

while True:
    line = f.stdout.readline()

    item = json.loads(line)
    send(item['to'],  item['msg'])   
    
    # sleep 2 detik
    time.sleep(2)
