import logging
import azure.functions as func
import socket
import traceback

def main(req: func.HttpRequest) -> func.HttpResponse:
    target_ip = "192.168.1.105"
    target_port = 80  # Change to 443 or whatever you want

    output = []
    output.append(f"📡 Ping check to {target_ip}:{target_port}")

    try:
        sock = socket.create_connection((target_ip, target_port), timeout=5)
        sock.close()
        output.append(f"PAIZEI MALAKA {target_ip}:{target_port} succeeded.")
        return func.HttpResponse("\n".join(output), status_code=200)
    except Exception as e:
        output.append(f"PAPARIA: {e}")
        output.append(traceback.format_exc())
        return func.HttpResponse("\n".join(output), status_code=404)
