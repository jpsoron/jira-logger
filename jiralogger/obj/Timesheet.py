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
        self.read_entries()

    def read_entries(self):
        excel_sheet = pandas.read_excel(self.filepath)

        #if sheet_size <= 1:
        #TODO

        for i in range(len(excel_sheet["Date (DD/MM/YYYY)"])):
            date = excel_sheet["Date (DD/MM/YYYY)"][i]
            date = date.strftime('%Y-%m-%d') + "T09:00:00.000-0300"
            if excel_sheet["JiraIgnore"][i] == True:
                entry = Entry(str(excel_sheet["Project"][i]), int(excel_sheet["Issue"][i]),
                              str(excel_sheet["Title"][i]), str(excel_sheet["Description"][i]),
                              date, float(excel_sheet["Hours"][i]), True)
                self.non_jira_entries.append(entry)
            else:
                entry = Entry(str(excel_sheet["Project"][i]), int(excel_sheet["Issue"][i]),
                              str(excel_sheet["Title"][i]), str(excel_sheet["Description"][i]),
                              date, float(excel_sheet["Hours"][i]), False)
                self.jira_entries.append(entry)

    def get_jira_entries(self):
        return self.jira_entries

    def get_non_jira_entries(self):
        return self.non_jira_entries

    def print(self):
        for i in range(len(self.jira_entries)):
            print("Entry " + str(i+1) + "\n" + self.jira_entries[i].get_project_name() + "-" +
                  str(self.jira_entries[i].get_issue_no()) + "\n")