import logging
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    url = "http://192.168.1.105"
    try:
        r = requests.get(url, timeout=5)
        return func.HttpResponse(f"Success {r.status_code}: {r.text[:200]}")
    except Exception as e:
        return func.HttpResponse(f"Connection failed: {str(e)}", status_code=500)
