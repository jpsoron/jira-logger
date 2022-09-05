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
        if date != date or date is None:
            continue
        project = sheet["Project"][i]
        if project != project or project is None:
            continue
        issue_num = sheet["Issue"][i]
        if issue_num != issue_num or issue_num is None:
            continue
        time_spent = sheet["TimeSpent"][i]
        if time_spent != time_spent or time_spent is None:
            continue

        time_remaining = sheet["TimeRemaining"][i]
        comment = sheet["Comment"][i]
        if comment is None or comment != comment:
            comment = ""
        #TODO agregar campo zona horaria
        worklog_entries.append(WorklogEntry(project, int(issue_num), date, float(time_spent), float(time_remaining), comment))
    return Timesheet(worklog_entries)