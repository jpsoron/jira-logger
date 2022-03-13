import pandas

from src.obj.Entry import Entry


class AllEntries:

    jira_entries = []
    non_jira_entries = []

    def __init__(self, filepath):
        self.filepath = filepath
        self.read_entries()

    def read_entries(self):
        excel_sheet = pandas.read_excel(self.filepath)
        for i in excel_sheet["Date"]:
            if excel_sheet["JiraIgnore"][i].__equals__("TRUE"):
                entry = Entry(excel_sheet["Project"][i], excel_sheet["Issue"][i],
                              excel_sheet["Title"][i], excel_sheet["Description"][i],
                              excel_sheet["Date"][i], excel_sheet["Hours"][i], True)
                self.non_jira_entries.append(entry)
            else:
                entry = Entry(excel_sheet["Project"][i], excel_sheet["Issue"][i],
                              excel_sheet["Title"][i], excel_sheet["Description"][i],
                              excel_sheet["Date"][i], excel_sheet["Hours"][i], False)
                self.jira_entries.append(entry)

    def get_jira_entries(self):
        return self.jira_entries

    def get_non_jira_entries(self):
        return self.non_jira_entries
