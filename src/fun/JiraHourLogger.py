import requests
from requests.auth import HTTPBasicAuth
import json

def jira_log_hours(email, api_token, jira_entries):
    auth = HTTPBasicAuth(email, api_token)
    responses = []
    for i in jira_entries:
        responses.append(log_entry(auth, jira_entries[i]))
    return responses

def log_entry(auth, current_entry):

    response = requests.request()
    return response