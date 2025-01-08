'''from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    payload: str

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/send")
def send_payload(data: InputData):
    return {"status": "success", "payload_received": data.payload}
'''


'''
#perfect code
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
import logging

# Initialize logging
logging.basicConfig(
    level=logging.DEBUG,  # Use DEBUG for detailed logs
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now; restrict in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load sensitive data from environment variables
API_KEY = os.getenv("VEXT_API_KEY", "9zCxU3jb.nmhDkkk94PQA27kUx6F6TTsKRw6lxXHy")
URL = os.getenv("VEXT_URL", "https://payload.vextapp.com/hook/13HDZDD8G7/catch/hello")

# Check if the API key or URL is missing
if not API_KEY or not URL:
    logging.error("Missing API_KEY or URL. Please ensure they are set correctly.")
    raise ValueError("API_KEY or URL is missing.")

headers = {
    "Content-Type": "application/json",
    "Apikey": f"Api-Key {API_KEY}"
}

# Define the input data model
class InputData(BaseModel):
    payload: str

# Root endpoint for health check
@app.get("/")
def root():
    logging.info("Root endpoint accessed.")
    return {"message": "API is running"}

# Endpoint to send payload to Vext API
@app.post("/send")
def send_payload(data: InputData):
    logging.debug("Received payload: %s", data.dict())
    logging.debug("Using headers: %s", headers)
    logging.debug("Using URL: %s", URL)

    try:
        # Send POST request to Vext API
        response = requests.post(URL, headers=headers, json=data.dict())

        # Log raw response details for debugging
        logging.debug("Raw response status: %s", response.status_code)
        logging.debug("Raw response content: %s", response.text)

        # Raise an HTTP exception for non-200 status codes
        response.raise_for_status()

        # Parse and log the response JSON
        response_json = response.json()
        logging.info("Parsed response JSON: %s", response_json)

        # Return structured response
        return {"status": "success", "data": response_json}

    except requests.exceptions.HTTPError as http_err:
        logging.error("HTTPError occurred: %s", http_err.response.text)
        raise HTTPException(
            status_code=http_err.response.status_code,
            detail=f"Vext API error: {http_err.response.text}"
        )
    except Exception as e:
        logging.exception("An unexpected error occurred.")
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected server error: {str(e)}"
        )

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()'''




from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
import logging

# Initialize logging
logging.basicConfig(
    level=logging.DEBUG,  # Use DEBUG for detailed logs
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now; restrict in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load sensitive data from environment variables
API_KEY = os.getenv("VEXT_API_KEY", "H0e4gjr6.0LG0g16NxaV7IPArQnmBETxEsrzzTdb6")  # Replace with your Vext API Key
URL = os.getenv("VEXT_URL", "https://payload.vextapp.com/hook/13HDZDD8G7/catch/hello")  # Replace with the correct URL

# Check if the API key or URL is missing
if not API_KEY or not URL:
    logging.error("Missing API_KEY or URL. Please ensure they are set correctly.")
    raise ValueError("API_KEY or URL is missing.")

headers = {
    "Content-Type": "application/json",
    "Apikey": f"Api-Key {API_KEY}"
}

# Define the input data model
class InputData(BaseModel):
    payload: str

# Root endpoint for health check
@app.get("/")
def root():
    logging.info("Root endpoint accessed.")
    return {"message": "API is running"}


@app.post("/send")
def send_payload(data: InputData):
    logging.debug("Received payload: %s", data.dict())
    logging.debug("Sending to Vext URL: %s", URL)
    logging.debug("Headers: %s", headers)

    try:
        response = requests.post(URL, headers=headers, json=data.dict())
        logging.debug("Vext response status: %s", response.status_code)
        logging.debug("Vext response content: %s", response.text)
        response.raise_for_status()
        response_json = response.json()
        return {"status": "success", "data": response_json}
    except requests.exceptions.HTTPError as http_err:
        logging.error("HTTPError occurred: %s", http_err.response.text)
        raise HTTPException(
            status_code=http_err.response.status_code,
            detail=f"Vext API error: {http_err.response.text}"
        )
    except Exception as e:
        logging.exception("An unexpected error occurred.")
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected server error: {str(e)}"
        )
