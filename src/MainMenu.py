from src.fun import JiraTimeLogger, TextGenerator
from src.obj.AllEntriesObject import AllEntriesObject

class MainMenu:

    def __init__(self, filepath, email, api_token, organization):
        self.email = email
        self.api_token = api_token
        self.organization = organization
        self.all_entries = AllEntriesObject(filepath)

    def jira_logger(self):
        entry_response_map = {}
        responses = JiraTimeLogger.jira_log_time(self.email, self.api_token, self.organization, self.all_entries.get_jira_entries())
        for i in range(len(responses)):
            entry_response_map[str(self.all_entries.jira_entries[i].to_string())] = str(responses[i].status_code)
        return entry_response_map

    def text_gen(self):
        TextGenerator.text_gen(self.all_entries.get_jira_entries(), self.all_entries.get_non_jira_entries())