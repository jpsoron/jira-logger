import os
import pprint

import pandas

from jiralogger.old.ProcessManager import ProcessManager


class MainMenu:

    """
    MainMenu class executes methods in the ProcessManager class according
    to user input. Acts as a UI of sorts.

    The object has a ProcessManager attribute as well as the credentials to access Jira.
    """

    """Constructor method reads credentials in credentials.csv file"""
    def __init__(self):
        self.ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '../..'))
        filepath = self.ROOT_DIR + "/files/credentials.csv"
        cred_file = pandas.read_csv(filepath)
        self.email = str(cred_file["Email"][0])
        self.api_token = cred_file["API Token"][0]
        self.organization = str(cred_file["Organization"][0]).lower()
        self.process_manager = ProcessManager(self.email, self.api_token, self.organization)

    """Main menu command line. Reads file when name is inputted by text."""
    def start(self):
        print("Welcome to JiraLogger.\n"
              "Remember to:\n"
              "-Enter credentials in /jira-logger/files/credentials.csv\n"
              "-Put timesheet files in /jira-logger/files/\n"
              "-----------------------------------------------------------\n")
        filename = input("Enter timesheet filename:")
        filepath = self.ROOT_DIR + "/files/" + filename
        statuscode = self.process_manager.read_timesheet(filepath)
        if statuscode == -1:
            print("Failed to read entries in such file.")
        while True:
            print("\n[1] Log hours on Jira\n"
                  "[2] Print timesheet\n")
            i = input()
            if i == "1":
                self.log_time()
                return
            elif i == "2":
                self.print_timesheet()
                return

    """Logs time on Jira from file read in start() method"""
    def log_time(self):
        response_map = self.process_manager.jira_logger()
        if response_map is None:
            print("No response from API. Check if filepath is correct or file is empty.")
        else:
            print("Time added to Jira. Request logs:\n")
            pprint.pprint(response_map)

    """Prints timesheet read in start() method"""
    def print_timesheet(self):
        print(self.process_manager.timesheet_tostring())


menu = MainMenu()
menu.start()