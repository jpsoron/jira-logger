import math

import pandas

from jiralogger.obj.Entry import Entry

class Timesheet:

    """
    Timesheet class has all information about worklogs.

    It contains two arrays of entries: jira and non-jira.
    """
    jira_entries = []
    non_jira_entries = []

    """Constructor method takes filepath as parameter and reads the file"""
    def __init__(self, filepath):
        self.filepath = filepath
        self.read_status = self.read_entries()

    """Reads entries in file given in constructor. Returns 1 if successful, -1 if there are no entries in file."""
    def read_entries(self):
        excel_sheet = pandas.read_excel(self.filepath)
        size = len(excel_sheet["Date (DD/MM/YYYY)"])
        if size <= 1:
            return -1
        for i in range(size):
            date = excel_sheet["Date (DD/MM/YYYY)"][i]
            date = date.strftime('%Y-%m-%d') + "T09:00:00.000-0300"
            if excel_sheet["JiraIgnore"][i] == True:
                # TODO tratar de mejorar performance y no tener mil chequeos
                # Cases where empty cells cause entry to be ommitted
                if pandas.isnull(excel_sheet["Hours"][i]):
                    continue
                else:
                    hours = float(excel_sheet["Hours"][i])
                if pandas.isnull(excel_sheet["Title"][i]):
                    # TODO caso a revisar
                    continue
                else:
                    title = str(excel_sheet["Title"][i])

                # Cases where empty cells don't affect entry
                if not pandas.isnull(excel_sheet["Description"][i]):
                    comment = str(excel_sheet["Description"][i])
                else:
                    comment = "None"
                entry = Entry(None, None, title, comment, date, hours, True)
                self.non_jira_entries.append(entry)
            else:

                # Cases where empty cells cause entry to be ommitted
                if pandas.isnull(excel_sheet["Project"][i]):
                    continue
                else:
                    project = str(excel_sheet["Project"][i])
                if pandas.isnull(excel_sheet["Issue"][i]):
                    continue
                else:
                    issue = int(excel_sheet["Issue"][i])
                if pandas.isnull(excel_sheet["Hours"][i]):
                    continue
                else:
                    hours = float(excel_sheet["Hours"][i])

                # Cases where empty cells don't affect entry
                if not pandas.isnull(excel_sheet["Title"][i]):
                    title = str(excel_sheet["Title"][i])
                else:
                    title = "None"
                if not pandas.isnull(excel_sheet["Description"][i]):
                    comment = excel_sheet["Description"][i]
                else:
                    comment = "None"
                entry = Entry(project, issue, title, comment, date, hours, False)
                self.jira_entries.append(entry)
        return 1

    def get_read_status(self):
        return self.read_status

    def get_jira_entries(self):
        return self.jira_entries

    def get_non_jira_entries(self):
        return self.non_jira_entries

    def print(self):
        for i in range(len(self.jira_entries)):
            print("Entry " + str(i+1) + "\n" + self.jira_entries[i].get_project_name() + "-" +
                  str(self.jira_entries[i].get_issue_no()) + "\n")