import requests
from requests.auth import HTTPBasicAuth
import json

def jira_log_hours(email, api_token, jira_entries):
    auth = HTTPBasicAuth(email, api_token)
    responses = []
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    for i in jira_entries:
        responses.append(log_entry(auth, jira_entries[i]), headers)
    return responses

def log_entry(auth, current_entry, headers):
    url = "https://ataway.atlassian.net/rest/api/2/issue/" + current_entry.get_project_name() + "-" + current_entry.get_issue_no() + "/worklog"

    payload = json.dumps({
        "timeSpentSeconds": current_entry.get_hours() * 3600,
        "comment": current_entry.get_description(),
        "started": current_entry.get_date()
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    return response