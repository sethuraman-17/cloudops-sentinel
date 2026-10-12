import json
import urllib.request
import urllib.error

URL = "http://127.0.0.1:8080/health"

try:
    with urllib.request.urlopen(URL, timeout=3) as response:
        healthy = response.status == 200
        status_code = response.status
        message = "Health endpoint responded successfully"

except urllib.error.HTTPError as error:
    healthy = False
    status_code = error.code
    message = f"HTTP error: {error.code}"

except Exception as error:
    healthy = False
    status_code = None
    message = str(error)

print(json.dumps({
    "url": URL,
    "application_healthy": healthy,
    "status_code": status_code,
    "message": message
}, indent=2))
