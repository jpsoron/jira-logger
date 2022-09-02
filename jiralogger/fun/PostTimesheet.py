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
        if worklog_entry.ignore is True:
            pass
        response = post_entry(auth, organization, headers, worklog_entry)
        responses.update({worklog_entry.project + str(worklog_entry.issue_num): response.status_code})
    return responses

def validate_non_duplicate(auth, organization, headers, worklog_entry):
    #TODO implement validation with API GET
    return

def post_entry(auth, organization, headers, worklog_entry):
    time_zone = worklog_entry.date.strftime("%z")
    date_time = worklog_entry.date.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
    if time_zone == "":
        formatted_entry_date = date_time + "-0300"
    else:
        formatted_entry_date = date_time + time_zone
    url = "https://" + organization + ".atlassian.net/rest/api/2/issue/" + worklog_entry.project + "-" + str(worklog_entry.issue_num) + "/worklog"
    payload = json.dumps({
        "timeSpentSeconds": float(worklog_entry.time_spent) * 3600,
        "comment": worklog_entry.comment,
        "started": formatted_entry_date
    })
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    return response