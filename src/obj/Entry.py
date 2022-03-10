class Entry:
    def __init__(self, project_name, issue_no, title, description, date, hours, jira_ignore):
        self.project_name = project_name
        self.issue_no = issue_no
        self.title = title
        self.description = description
        self.date = date
        self.hours = hours
        self.jira_ignore = jira_ignore
        pass

    def get_project_name(self):
        return self.project_name

    def get_issue_no(self):
        return self.issue_no

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_date(self):
        return self.date

    def get_hours(self):
        return self.hours

    def jira_ignore(self):
        return self.jira_ignore
