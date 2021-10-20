class WeeklyHours:
    def __init__(self):
        self.dailyhourlist = []

    def get_daily_hours(self):
        return self.dailyhourlist

    def add_daily_hours(self, dailyhours):
        self.dailyhourlist.append(dailyhours)


class DailyHours:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_entries(self):
        return self.entries


class Entry:
    def __init__(self, name, jiraload, projectid, ticketid, duration, date):
        self.name = name
        self.jiraload = jiraload
        self.projectid = projectid
        self.ticketid = ticketid
        self.duration = duration
        self.date = date

    def get_name(self):
        return self.name

    def jira_load(self):
        return self.jiraload

    def get_projectid(self):
        return self.projectid

    def get_ticketid(self):
        return self.ticketid

    def get_duration(self):
        return self.duration

    def get_date(self):
        return self.date


