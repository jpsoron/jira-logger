from src.fun import JiraTimeLogger, TextGenerator
from src.obj.AllEntriesObject import AllEntries

class MainMenu:

    responses = []

    def __init__(self, filepath):
        self.all_entries = AllEntries(filepath)

    def jira_logger(self, email, api_token, organization):
        self.responses = JiraTimeLogger.jira_log_time(email, api_token, organization, self.all_entries.get_jira_entries())

    def jira_validate_changes(self):
        failed_changes = []
        for i in range(len(self.responses)):
            if self.responses[i].status_code != 201:
                failed_changes.append(self.responses[i])
        if not failed_changes:
            return None
        return failed_changes

    def text_gen(self):
        TextGenerator.text_gen(self.all_entries.get_jira_entries(), self.all_entries.get_non_jira_entries())