import os
import requests
from flask import Flask
from threading import Thread
import time
from datetime import datetime

app = Flask("pyrepl")

@app.route('/')
def home():
	return "this repl is using <b>pyrepl</b> by <a href='https://bit.ly/0Midnite'>0Midnite</a>"

def server():
    app.run(host="0.0.0.0", port=7079)

Thread(target=server).start()

repl_owner = os.getenv('REPL_OWNER')
repl_slug = os.getenv('REPL_SLUG')
replit_url = f"https://{repl_slug}.{repl_owner}.repl.co"

def pyrepl():
    while True:
        res = requests.get(replit_url, headers={"pyrepl": "something"})
        if res.request.headers["pyrepl"]:
            print(f'[{datetime.now()}] [pyrepl] your repl was pinged')
        time.sleep(30)
    
Thread(target=pyrepl).start()
