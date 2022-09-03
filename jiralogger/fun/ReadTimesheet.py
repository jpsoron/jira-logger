import datetime
import math

import pandas
import numbers

from jiralogger.obj.Timesheet import WorklogEntry, Timesheet


def read_timesheet(timesheet_path):
    worklog_entries = []
    sheet = pandas.read_excel(timesheet_path)
    size = len(sheet["Date"])
    for i in range(size):
        # IGNORES ENTRY IF FLAGGED
        if sheet["Ignore"][i] == 1:
            continue

        # DATA VALIDATION
        date = sheet["Date"][i]
        if date is None or not isinstance(date, datetime.datetime):
            continue
        project = sheet["Project"][i]
        if project is None or project != project:
            continue
        issue_num = sheet["Issue"][i]
        if issue_num is None or issue_num != issue_num:
            continue
        time_spent = sheet["TimeSpent"][i]
        if time_spent is None or not isinstance(time_spent, numbers.Number):
            continue

        time_remaining = sheet["TimeRemaining"][i]
        comment = sheet["Comment"][i]
        if comment is None:
            comment = ""
        #TODO agregar campo zona horaria
        worklog_entries.append(WorklogEntry(False, project, int(issue_num), date, time_spent, float(time_remaining), comment))
    return Timesheet(worklog_entries)
