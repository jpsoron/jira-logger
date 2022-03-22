import os
import pprint

import pandas

from jiralogger.ProcessManager import ProcessManager


class MainMenu:

    def __init__(self):
        self.ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
        filepath = self.ROOT_DIR + "/files/credentials.csv"
        cred_file = pandas.read_csv(filepath)
        self.email = str(cred_file["Email"][0])
        self.api_token = cred_file["API Token"][0]
        self.organization = str(cred_file["Organization"][0]).lower()
        self.process_manager = ProcessManager(self.email, self.api_token, self.organization)

    def start(self):
        print("Welcome to JiraLogger.\n"
              "Remember to:\n"
              "-Enter credentials in /jira-logger/files/credentials.csv\n"
              "-Put timesheet files in /jira-logger/files/\n"
              "-----------------------------------------------------------\n")
        filename = input("Enter timesheet filename:")
        filepath = self.ROOT_DIR + "/files/" + filename
        self.process_manager.read_timesheet(filepath)
        response_map = self.process_manager.jira_logger()
        if response_map is None:
            print("No response from API. Check if filepath is correct or file is empty.")
        else:
            print("Time added to Jira. Request logs:\n")
            pprint.pprint(response_map)

    def log_time(self):
        #Not used
        filename = input("Enter filename:")
        filepath = self.ROOT_DIR + "/files/" + filename
        self.process_manager.read_timesheet(filepath)
        return

    def print_timesheet(self):
        print(self.process_manager.print_timesheet())

    def txt_gen(self):
        print(self.process_manager.txt_gen())


menu = MainMenu()
menu.start()