import logging
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Function triggered")

    url = "http://192.168.1.105"
    try:
        response = requests.get(url, timeout=5)
        logging.info(f"Success: {response.status_code}")
        return func.HttpResponse(f"Success: {response.status_code}\n{response.text[:200]}")
    except Exception as e:
        logging.error(f"Exception during request: {str(e)}")
        return func.HttpResponse(f"Connection failed: {str(e)}", status_code=500)
