from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime, timezone
import json

LOG_FILE = "app.log"

def write_log(level, message):
    timestamp = datetime.now(timezone.utc).isoformat()
    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} {level} {message}\n")

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            write_log("INFO", "Health check successful")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            response = {
                "status": "healthy",
                "application": "CloudOps Sentinel Demo"
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            write_log("WARNING", f"Unknown endpoint requested: {self.path}")
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", 8080), HealthHandler)

print("CloudOps Sentinel demo app running on 127.0.0.1:8080")
print("Logs are being written to app.log")

server.serve_forever()
