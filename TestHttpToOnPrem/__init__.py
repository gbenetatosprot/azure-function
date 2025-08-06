import logging
import azure.functions as func
import socket
import traceback

try:
    import requests
except ImportError:
    requests = None

def main(req: func.HttpRequest) -> func.HttpResponse:
    target_host = "192.168.1.105"
    target_port = 80
    url = f"http://{target_host}"

    output = []
    output.append("🔍 Starting debug check...")

    # 1. Check for 'requests' availability
    if requests is None:
        output.append("❌ 'requests' library not found. Add it to requirements.txt.")
        return func.HttpResponse("\n".join(output), status_code=500)

    # 2. TCP Connectivity Test
    try:
        output.append(f"🔌 Trying TCP connect to {target_host}:{target_port}...")
        sock = socket.create_connection((target_host, target_port), timeout=5)
        sock.close()
        output.append(f"✅ TCP connection to {target_host}:{target_port} succeeded.")
    except Exception as e:
        output.append(f"❌ TCP connection failed: {e}")
        output.append(traceback.format_exc())
        return func.HttpResponse("\n".join(output), status_code=404)

    # 3. HTTP GET Test
    try:
        output.append(f"🌐 Trying HTTP GET {url} ...")
        resp = requests.get(url, timeout=5)
        output.append(f"✅ HTTP GET succeeded: {resp.status_code}")
        output.append(f"🧾 Body (first 200 chars):\n{resp.text[:200]}")
        return func.HttpResponse("\n".join(output), status_code=200)
    except Exception as e:
        output.append(f"❌ HTTP GET failed: {e}")
        output.append(traceback.format_exc())
        return func.HttpResponse("\n".join(output), status_code=404)
