import datetime, time

import requests
import pandas
from requests.auth import HTTPBasicAuth
import json


def post_timesheet(email, api_token, organization, timesheet):
    auth = HTTPBasicAuth(email, api_token)
    response_log = ""
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    account_id = get_self_userid(auth, organization, headers)
    worklog_entries = timesheet.get_worklog_entries()
    for worklog_entry in worklog_entries:
        project = worklog_entry.project
        issue_num = worklog_entry.issue_num
        time_spent_seconds = worklog_entry.time_spent * 3600
        comment = worklog_entry.comment
        started_date = worklog_entry.date.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "-0300"
        started_after_param = unix_time_convert(worklog_entry.date - datetime.timedelta(seconds=1))
        started_before_param = unix_time_convert(worklog_entry.date + datetime.timedelta(seconds=1))

        if validate_non_duplicate(auth, organization, headers, account_id, project, issue_num, time_spent_seconds, comment, started_after_param, started_before_param):
            response = post_entry(auth, organization, headers, project, issue_num, time_spent_seconds, comment, started_date)
            print("Entry: {" + started_date + " " + project + "-" + str(issue_num) + ": " + str(comment) + "}" + " Status: " + "{" + str(response.status_code) + "}")
        else:
            print("Entry: {" + started_date + " " + project + "-" + str(issue_num) + ": " + str(comment) + "}" + " Status: " + "{DUPLICATE ENTRY}")


def post_entry(auth, organization, headers, project, issue_num, time_spent_seconds, comment, started_date):
    payload = json.dumps({
        "timeSpentSeconds": time_spent_seconds,
        "comment": comment,
        "started": started_date
    })
    response = requests.request(
        "POST",
        url="https://" + organization + ".atlassian.net/rest/api/2/issue/" + project + "-" + str(issue_num) + "/worklog",
        data=payload,
        headers=headers,
        auth=auth
    )
    return response


def validate_non_duplicate(auth, organization, headers, account_id, project, issue_num, time_spent_seconds, comment, started_after, started_before):

    response = requests.request(
        "GET",
        url="https://" + organization + ".atlassian.net/rest/api/2/issue/" + project + "-" + str(issue_num) + "/worklog?startedAfter=" + str(started_after) + "&" + str(started_before),
        headers=headers,
        auth=auth
    )

    issue_worklogs = json.loads(response.text)["worklogs"]
    for worklog in issue_worklogs:
        if (worklog["author"]["accountId"] == account_id) and (str(worklog["comment"]) == comment) and (worklog["timeSpentSeconds"] == time_spent_seconds):
            return False
    return True


def unix_time_convert(timestamp):
    return int(time.mktime(timestamp.timetuple()) * 1e3 + timestamp.microsecond / 1e3)


def get_self_userid(auth, organization, headers):
    response = requests.request(
        "GET",
        url="https://" + organization + ".atlassian.net/rest/api/2/myself",
        headers=headers,
        auth=auth
    )
    return json.loads(response.text)["accountId"]