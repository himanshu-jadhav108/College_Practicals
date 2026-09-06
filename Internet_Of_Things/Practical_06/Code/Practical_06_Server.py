# Practical 6: HTTP REST Server in Python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import datetime

class SensorHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        data = json.loads(self.rfile.read(length))
        t = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{t}] Server received -> {data}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"status": "OK"}')

    def log_message(self, format, *args):
        pass  # silence default logging

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8080), SensorHandler)
    print("Server listening on http://127.0.0.1:8080")
    server.serve_forever()
