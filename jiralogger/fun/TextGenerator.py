def text_gen(jira_entries, non_jira_entries):
    text = ""
    for i in range(len(jira_entries)):
        if jira_entries[i].get_date() != jira_entries[i-1].get_date():
            text += str(jira_entries[i].get_date()) + "\n"
        text += jira_entry_tostring(jira_entries[i])
    for n in range(len(non_jira_entries)):
        if jira_entries[n].get_date() != jira_entries[n-1].get_date():
            text += str(jira_entries[n].get_date()) + "\n"
        text += non_jira_entry_tostring(non_jira_entries[n])
    return text

def jira_entry_tostring(entry):
    str(entry.get_project_name()) + "-" + str(entry.get_issue_no()) + ": D:" + str(entry.get_hours()) + "||C:null||" + str(entry.get_title()) + "(" + str(entry.get_comment()) + ")"

def non_jira_entry_tostring(entry):
    str(entry.get_title) + " " + str(entry.get_hours()) + "h (" + str(entry.get_comment()) + ")"