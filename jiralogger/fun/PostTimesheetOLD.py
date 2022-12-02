import datetime, time

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
        responses.update({worklog_entry.project + "-" + str(worklog_entry.issue_num) + " " + worklog_entry.comment + " " + worklog_entry.date.strftime("%Y-%m-%dT%H:%M:%S.%f"): response.status_code})
    return responses


def post_entry(auth, organization, headers, worklog_entry):
    payload = json.dumps({
        "timeSpentSeconds": worklog_entry.time_spent * 3600,
        "comment": worklog_entry.comment,
        "started": worklog_entry.date.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "-0300"
    })
    response = requests.request(
        "POST",
        url="https://" + organization + ".atlassian.net/rest/api/2/issue/" + worklog_entry.project + "-" + str(worklog_entry.issue_num) + "/worklog",
        data=payload,
        headers=headers,
        auth=auth
    )
    return response
