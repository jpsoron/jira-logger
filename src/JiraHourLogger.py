import requests
from requests.auth import HTTPBasicAuth
import json

def jira_log_hours(email, api_token, jira_entries):
    auth = HTTPBasicAuth(email, api_token)

    pass

def log_entry(auth, jira_entry):
    pass