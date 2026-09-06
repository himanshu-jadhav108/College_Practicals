# Practical 6: HTTP Sensor Client in Python
import urllib.request
import json
import random
import time

URL = "http://127.0.0.1:8080/data"

def read_sensor():
    return round(random.uniform(24.0, 32.0), 1)

for i in range(1, 6):
    payload = {"device_id": "node01", "reading_no": i, "temperature": read_sensor()}
    req = urllib.request.Request(URL, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        print(f"Device sent -> {payload} | Server reply: {r.read().decode()}")
    time.sleep(1)
print("Transmission complete")
