import requests
import time

URL = "https://sasdsxa-2.onrender.com"  # حط رابط البوت هنا

while True:
    try:
        res = requests.get(URL)
        print(f"Pinged {URL}, Status: {res.status_code}")
    except Exception as e:
        print(f"Error pinging: {e}")
    time.sleep(300)  # كل 5 دقايق