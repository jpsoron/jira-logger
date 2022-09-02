class Timesheet:

    worklog_entries = []

    def __init__(self, worklog_entries):
        self.worklog_entries = worklog_entries

    def get_worklog_entries(self):
        return self.worklog_entries

    def add_entry(self, entry):
        self.worklog_entries.append(entry)

    def to_string(self):
        to_string = ""
        i = 0
        for entry in self.worklog_entries:
            i += 1
            to_string += "Worklog Entry " + str(i) + ": \nIssue: " + str(entry.project) + "-" + str(int(entry.issue_num)) + "\nDate: " + str(entry.date) + "\nTime spent: " + str(entry.time_spent) + "\nTime remaining: " + str(entry.time_remaining) + "\nComment: " + str(entry.comment) + "\n\n"
        return to_string

class WorklogEntry:

    def __init__(self, ignore, project, issue_num, date, time_spent, time_remaining, comment):
        self.ignore = ignore
        self.project = project
        self.issue_num = issue_num
        self.date = date
        self.time_spent = time_spent
        self.time_remaining = time_remaining
        self.comment = comment

