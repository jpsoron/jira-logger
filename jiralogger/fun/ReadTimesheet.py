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
        if sheet["Ignore"][i] is True:
            pass
        date = sheet["Date"][i]
        project = sheet["Project"][i]
        issue_num = sheet["Issue"][i]
        time_spent = sheet["TimeSpent"][i]
        time_remaining = sheet["TimeRemaining"][i]
        comment = sheet["Comment"][i]
        valid = data_validation(date, time_spent, time_remaining, project, issue_num)
        if comment is None:
            comment = ""
        #TODO agregar campo zona horaria
        if valid is True:
            worklog_entries.append(WorklogEntry(False, project, int(issue_num), date, float(time_spent), float(time_remaining), comment))
    return Timesheet(worklog_entries)

def data_validation(date, time_spent, time_remaining, project, issue_num):
    # Checking required fields
    if date is None or not isinstance(date, datetime.datetime):
        return False
    if project is None or project != project:
        return False
    if issue_num is None or issue_num != issue_num:
        return False
    if time_spent is None or not isinstance(time_spent, numbers.Number):
        return False
    return True