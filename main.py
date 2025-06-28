
import threading
import time
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Ping bot is running!"

def keep_alive():
    def run():
        app.run(host='0.0.0.0', port=8080)
    t = threading.Thread(target=run)
    t.start()

keep_alive()

while True:
    try:
        requests.get("https://sasdsxa-2.onrender.com")
        print("✅ Ping sent.")
    except Exception as e:
        print("❌ Ping failed:", e)
    time.sleep(60)
