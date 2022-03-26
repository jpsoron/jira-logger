class Entry:

    """
    Entry class contains information about a single timesheet entry.

    Includes project name, issue number, title, comment, date,
    amount of hours and a boolean jiraignore flag.
    """

    """Constructor takes all attributes as parameters"""
    def __init__(self, project_name, issue_no, title, comment, date, hours, jira_ignore):
        self.project_name = project_name
        self.issue_no = issue_no
        self.title = title
        self.comment = comment
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

    def get_comment(self):
        return self.comment

    def get_date(self):
        return self.date

    def get_hours(self):
        return self.hours

    def jira_ignore(self):
        return self.jira_ignore

    def to_string(self):
        return str(self.date) + " // " + str(self.project_name) + "-" + str(self.issue_no)