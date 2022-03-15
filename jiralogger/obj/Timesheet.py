import pandas

from jiralogger.obj.Entry import Entry

class Timesheet:

    jira_entries = []
    non_jira_entries = []

    def __init__(self, filepath):
        self.filepath = filepath
        self.read_entries()

    def read_entries(self):
        excel_sheet = pandas.read_excel(self.filepath)

        #if sheet_size <= 1:
        #TODO

        for i in range(len(excel_sheet["Date"])):
            date = excel_sheet["Date"][i]
            date = date.strftime('%Y-%m-%d') + "T00:00:00.000+0000"
            if excel_sheet["JiraIgnore"][i] == "TRUE":
                entry = Entry(excel_sheet["Project"][i], excel_sheet["Issue"][i],
                              excel_sheet["Title"][i], excel_sheet["Description"][i],
                              date, excel_sheet["Hours"][i], True)
                self.non_jira_entries.append(entry)
            else:
                entry = Entry(excel_sheet["Project"][i], excel_sheet["Issue"][i],
                              excel_sheet["Title"][i], excel_sheet["Description"][i],
                              date, excel_sheet["Hours"][i], False)
                self.jira_entries.append(entry)

    def get_jira_entries(self):
        return self.jira_entries

    def get_non_jira_entries(self):
        return self.non_jira_entries

    def print(self):
        for i in range(len(self.jira_entries)):
            print("Entry " + str(i+1) + "\n" + str(self.jira_entries[i].get_project_name()) + "-" +
                      str(self.jira_entries[i].get_issue_no()) + "\n")