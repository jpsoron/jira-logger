import datetime

import pandas
import numbers

from jiralogger.obj.Timesheet import WorklogEntry, Timesheet


def read_timesheet(timesheet_path):
    worklog_entries = []
    sheet = pandas.read_excel(timesheet_path)
    size = len(sheet["Date (DD/MM/YYYY)"])
    for i in range(size):
        date = sheet["Date (DD/MM/YYYY)"][i]
        project = sheet["Project"][i]
        issue_num = sheet["Issue"][i]
        time_spent = sheet["TimeSpent"][i]
        time_remaining = sheet["TimeRemaining"][i]
        comment = sheet["Comment"][i]
        ignore = sheet["Ignore"][i]
        valid = data_validation(date, time_spent, time_remaining, project)
        if comment is None:
            comment = ""
        #TODO arregla este chequeo nefasto
        if isinstance(date, datetime.datetime):
            time_zone = date.strftime("%z")
            date_time = date.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
            if time_zone == "":
                date = date_time + "+0000"
            else:
                date = date_time + time_zone
        if valid and ignore is not True:
            worklog_entries.append(WorklogEntry(ignore, project, issue_num, date, time_spent, time_remaining, comment))
            #TODO poner chequeo de ignore adelante de todo para mejorar perf
        else:
            #TODO generar log de entries que no pasan
            pass
    return Timesheet(worklog_entries)

def data_validation(date, time_spent, time_remaining, project):
    # Checking required fields
    if date is None:
        #TODO tambien chequear si fecha esta en formato incorrecto
        return False
    if project is None:
        return False
    if time_spent is None or not isinstance(time_spent, numbers.Number):
        return False
    if time_remaining is not None and not isinstance(time_remaining, numbers.Number):
        return False
    return True