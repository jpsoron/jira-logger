from jiralogger.fun.TimesheetToString import timesheet_tostring
from jiralogger.fun.JiraTimeLogger import jira_log_time
from jiralogger.obj.Timesheet import Timesheet

class ProcessManager:

    """
    ProcessManager class has a Timesheet object. Once read_timesheet() method is called,
    ProcessManager can log time to Jira or print said timesheet.
    """

    """Constructor takes Jira credentials as parameters"""
    def __init__(self, email, api_token, organization):
        self.email = email
        self.api_token = api_token
        self.organization = organization
        self.timesheet = None

    """Method to read timesheet in specified filepath and write to a Timesheet object."""
    def read_timesheet(self, filepath):
        self.timesheet = Timesheet(filepath)
        if self.timesheet.get_read_status() == -1:
            return -1
        else:
            return 1

    """Method to log timesheet to Jira. Returns map with issue codes and status codes
    to check if API requests were successful."""
    def jira_logger(self):
        entry_response_map = {}
        if self.timesheet is None:
            return None
        responses = jira_log_time(self.email, self.api_token, self.organization, self.timesheet.jira_entries)
        for i in range(len(responses)):
            entry_response_map[self.timesheet.jira_entries[i].to_string()] = str(responses[i].status_code)
        return entry_response_map

    """Method to print timesheet on screen"""
    def timesheet_tostring(self):
        return timesheet_tostring(self.timesheet.get_jira_entries(), self.timesheet.get_non_jira_entries())