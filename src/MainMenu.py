import pandas

from src import TextGen, JiraLoader
from src.obj.Entry import Entry

def start():
    all_entries = AllEntries("Sample")
    

class AllEntries:

    jira_entries = []
    non_jira_entries = []

    def __init__(self, filepath):
        self.filepath = filepath
        self.read_entries()
        pass

    def read_entries(self):
        excel_sheet = pandas.read_excel(self.filepath)
        for i in self.excel_sheet["Date"]:
            if self.excel_sheet["JiraIgnore"][i].__equals__("TRUE"):
                entry = Entry(self.excel_sheet["Project"][i], self.excel_sheet["Issue"][i],
                              self.excel_sheet["Title"][i], self.excel_sheet["Description"][i],
                              self.excel_sheet["Date"][i], self.excel_sheet["Hours"][i], True)
                self.non_jira_entries.append(entry)
            else:
                entry = Entry(self.excel_sheet["Project"][i], self.excel_sheet["Issue"][i],
                              self.excel_sheet["Title"][i], self.excel_sheet["Description"][i],
                              self.excel_sheet["Date"][i], self.excel_sheet["Hours"][i], False)
                self.jira_entries.append(entry)

    def get_jira_entries(self):
        return self.jira_entries

    def get_non_jira_entries(self):
        return self.non_jira_entries
