import requests
from requests.auth import HTTPBasicAuth
import json

def jira_log_time(email, api_token, organization, jira_entries):
    auth = HTTPBasicAuth(email, api_token)
    responses = []
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    for i in range(len(jira_entries)):
        responses.append(log_entry(auth, organization, jira_entries[i], headers))
    return responses

def log_entry(auth, organization, current_entry, headers):
    url = "https://" + str(organization) + ".atlassian.net/rest/api/2/issue/" + str(current_entry.get_project_name()) + "-" + str(current_entry.get_issue_no()) + "/worklog"

    payload = json.dumps({
        "timeSpentSeconds": current_entry.get_hours() * 3600,
        "comment": current_entry.get_comment(),
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