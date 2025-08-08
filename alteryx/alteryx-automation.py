import requests
#import json
from requests.auth import HTTPBasicAuth
import os

# ALTERYX_SERVER = "https://your-alteryx-server.com/gallery/api"
# API_KEY = "your-api-key"
# API_SECRET = "your-api-secret"

ALTERYX_SERVER = os.getenv("ALTERYX_SERVER_URL")
API_KEY = os.getenv("ALTERYX_API_KEY")
API_SECRET = os.getenv("ALTERYX_API_SECRET")


def get_access_token():
    url = f"{ALTERYX_SERVER}/auth/token/"
    response = requests.post(url, auth=HTTPBasicAuth(API_KEY, API_SECRET))
    response.raise_for_status()
    return response.json()['access_token']



# def get_alteryx_workflow_status(workflow_id, api_key, base_url='https://your-alteryx-server.com/api'):
#     """
#     Fetch the status of an Alteryx workflow using its ID.

#     :param workflow_id: The ID of the workflow to check.
#     :param api_key: Your API key for authentication.
#     :param base_url: The base URL of your Alteryx server API.
#     :return: JSON response containing the workflow status.
#     """
#     headers = {
#         'Authorization': f'Bearer {api_key}',
#         'Content-Type': 'application/json'
#     }
    
#     url = f"{base_url}/workflows/{workflow_id}/status"
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         response.raise_for_status()


