import requests
import pandas
from requests.auth import HTTPBasicAuth
import json

def post_timesheet(email, api_token, organization, timesheet):
    auth = HTTPBasicAuth(email, api_token)
    responses = {}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    worklog_entries = timesheet.get_worklog_entries()
    for worklog_entry in worklog_entries:
        response = post_entry(auth, organization, headers, worklog_entry)
        responses.update({worklog_entry.project + str(worklog_entry.issue_num): response.status_code})
    return responses

def post_entry(auth, organization, headers, worklog_entry):

    #TODO chequear que no este duplicado con un GET al API

    url = "https://" + organization + ".atlassian.net/rest/api/2/issue/" + worklog_entry.project + "-" + str(worklog_entry.issue_num) + "/worklog"
    payload = json.dumps({
        "timeSpentSeconds": int(worklog_entry.time_spent) * 3600,
        "comment": worklog_entry.comment,
        "started": worklog_entry.date
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    return response