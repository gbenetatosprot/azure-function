import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Function triggered successfully.")
    return func.HttpResponse(" Function executed successfully!", status_code=200)