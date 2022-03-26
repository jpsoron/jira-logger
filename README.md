# jira-logger

Simple and easy to use program to log hours on Jira issue worklogs. Program reads excel files in specific format and automatically logs 
time to corresponding issues.

## Setup

**Note:** You need to have Python 3.x installed and added to your local PATH variable.

1. Run the install.bat script. 
2. Go to /files/. This will be the folder where your credentials and timesheets will be located.
3. Make a new file called "credentials.csv", copying the format from the "sample_credentials.csv" file and filling in your data.

## Making Timesheet Files

To create an excel file to log time, copy the sample_timesheet.xlsx file in /files/ and fill it in with your own entries. 
You can create multiple files to log your work at different times (for example one might choose to make a file for every 
week, and use the script at the end of the week to log it on Jira)

**Make sure your timesheet file has the same format as sample_timesheet.xlsx.** Below are some tips and tricks:

- Dates must always be in DD/MM/YYYY format
- If you wish to add an entry in the file, but don't want to log it onto Jira, enter TRUE in the JiraIgnore field on the 
file. Otherwise leave it blank.
- For non Jira entries, the Project and Issue fields are optional

## Using the Script

Having made the file you wish to use the script on, follow the next steps:
1. Launch the start.bat script
2. Enter the name of the excel file
3. Enter 1 to log all entries in the file to Jira, or 2 to print the timesheet
