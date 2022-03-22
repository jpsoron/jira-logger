from jiralogger.fun import JiraTimeLogger, TextGenerator
from jiralogger.obj.Timesheet import Timesheet

class ProcessManager:

    def __init__(self, email, api_token, organization):
        self.email = email
        self.api_token = api_token
        self.organization = organization
        self.all_entries = None

    def read_timesheet(self, filepath):
        self.all_entries = Timesheet(filepath)

    def jira_logger(self):
        entry_response_map = {}
        if self.all_entries is None:
            return None
        responses = JiraTimeLogger.jira_log_time(self.email, self.api_token, self.organization, self.all_entries.get_jira_entries())
        for i in range(len(responses)):
            entry_response_map[str(self.all_entries.jira_entries[i].to_string())] = str(responses[i].status_code)
        return entry_response_map

    def print_timesheet(self):
        #TODO
        return

    def txt_gen(self):
        return TextGenerator.text_gen(self.all_entries.get_jira_entries(), self.all_entries.get_non_jira_entries())