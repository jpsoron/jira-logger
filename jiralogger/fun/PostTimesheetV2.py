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
    account_id = get_self_userid(auth, organization, headers)
    worklog_entries = timesheet.get_worklog_entries()
    for worklog_entry in worklog_entries:
        if validate_non_duplicate(auth, organization, headers, account_id, worklog_entry):
            response = post_entry(auth, organization, headers, worklog_entry)
            responses.update({worklog_entry.project + str(worklog_entry.issue_num): response.status_code})
        else:
            #TODO implement failed case
            print("DUPLICATE ENTRY")
            break
    return responses

def validate_non_duplicate(auth, organization, headers, account_id, worklog_entry):
    #TODO implement validation with API GET

    started_after_param = convert_timestamp_to_unix(worklog_entry.date - datetime.timedelta(hours=1))
    started_before_param = convert_timestamp_to_unix(worklog_entry.date + datetime.timedelta(hours=1))

    worklog_time_zone = worklog_entry.date.strftime("%z")
    worklog_date_time = worklog_entry.date.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
    if worklog_time_zone == "":
        formatted_entry_date = worklog_date_time + "-0300"
    else:
        formatted_entry_date = worklog_date_time + worklog_time_zone

    url = "https://" + organization + ".atlassian.net/rest/api/2/issue/" + worklog_entry.project + "-" + str(worklog_entry.issue_num) + "/worklog?startedAfter=" + str(started_after_param) + "&" + str(started_before_param)
    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    print(str(started_after_param))
    print(str(started_before_param))
    print(response)
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

    worklogs = json.loads(response.text)["worklogs"]
    for worklog in worklogs:
        print(worklog["author"]["accountId"])
        print(worklog["comment"])
        print(worklog["started"])
        print(worklog["timeSpent"])

        time_spent_td = datetime.timedelta(hours=worklog_entry.time_spent)
        time_spent_formatted = str(time_spent_td.seconds//3600) + "h " + str((time_spent_td.seconds//60)%60) + "m"

        if (worklog["author"]["accountId"] == account_id):
            print("duplicate account id")
        if str(worklog["comment"] == worklog_entry.comment):
            print("duplicate comment")
        if (worklog["started"] == formatted_entry_date):
            print("duplicate started date")
        if (worklog["timeSpent"] == time_spent_formatted):
            print("duplicate timespent")

    return True

def convert_timestamp_to_unix(timestamp):
    return int(time.mktime(timestamp.timetuple()) * 1e3 + timestamp.microsecond / 1e3)

def get_self_userid(auth, organization, headers):
    url = "https://" + organization + ".atlassian.net/rest/api/2/myself"
    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    return json.loads(response.text)["accountId"]

def post_entry(auth, organization, headers, worklog_entry):

    url = "https://" + organization + ".atlassian.net/rest/api/2/issue/" + worklog_entry.project + "-" + str(worklog_entry.issue_num) + "/worklog"
    payload = json.dumps({
        "timeSpentSeconds": float(worklog_entry.time_spent) * 3600,
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