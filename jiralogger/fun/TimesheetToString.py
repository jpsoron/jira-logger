"""
Method to return a string with a timesheet's details.
"""
def timesheet_tostring(jira_entries, non_jira_entries):
    text = "My timesheet\n" \
           "Jira entries: \n"
    for i in range(len(jira_entries)):
        current = jira_entries[i]
        currentdate = current.get_date()
        if i == 0 or currentdate != jira_entries[i-1].get_date():
            text += str(currentdate) + "\n"
        text += jira_entry_tostring(current)
    text += "\nNon-Jira entries:\n"
    for n in range(len(non_jira_entries)):
        current = non_jira_entries[n]
        currentdate = current.get_date()
        if n == 0 or currentdate != jira_entries[n-1].get_date():
            text += str(currentdate) + "\n"
        text += non_jira_entry_tostring(current)
    return text

def jira_entry_tostring(entry):
    return entry.get_project_name() + "-" + str(entry.get_issue_no()) + ": " + str(entry.get_hours()) + "h " \
           + entry.get_title() + " (" + entry.get_comment() + ")\n"

def non_jira_entry_tostring(entry):
    return str(entry.get_hours()) + "h " + entry.get_title() + " (" + entry.get_comment() + ")" + "\n"