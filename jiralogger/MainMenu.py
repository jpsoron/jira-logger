from pathlib import Path
from inspect import getsourcefile
from os.path import abspath
from jiralogger.fun import ReadTimesheet, PostTimesheet
import os

import pandas


class MainMenu:
    def __init__(self):
        self.organization = ""
        self.api_token = ""
        self.email = ""
        current_file_path = abspath(getsourcefile(lambda: 0))
        self.jiralogger_directory = current_file_path.replace("MainMenu.py","")
        self.files_directory = os.path.join(self.jiralogger_directory + "../files")
        return

    def main_menu(self):
        print("WELCOME TO JIRALOGGER\n-------------")
        self.read_credentials()
        while True:
            print("[1] Log timesheet to Jira\n"
                  "[2] Update credentials"
                  )
            user_input = input()
            if user_input == "1":
                self.log_timesheet()
            elif user_input == "2":
                self.update_credentials()
            else:
                break

    def log_timesheet(self):
        user_input = input("\nEnter timesheet file name: ")
        timesheet_path = os.path.join(self.files_directory, user_input)
        timesheet = self.read_timesheet(timesheet_path)
        self.post_timesheet(timesheet)

    def read_timesheet(self, timesheet_path):
        return ReadTimesheet.read_timesheet(timesheet_path)

    def post_timesheet(self, timesheet):
        PostTimesheet.post_timesheet(self.email, self.api_token, self.organization, timesheet)
        print("---Timesheet P0ST complete. Press enter to continue---\n")
        # TODO validacion de codigos del request
        return

    def read_credentials(self):
        filepath = os.path.join(self.files_directory, "credentials.csv")
        credentials_file = pandas.read_csv(filepath)

        if len(credentials_file["Email"]) == 0:
            print("API credentials are empty. Please fill them out below: ")
            self.update_credentials()
        else:
            self.email = str(credentials_file["Email"][0])
            self.api_token = str(credentials_file["API Token"][0])
            self.organization = str(credentials_file["Organization"][0])

    def update_credentials(self):
        filepath = os.path.join(self.files_directory, "credentials.csv")
        credentials_file = pandas.read_csv(filepath)
        print("Enter your email:")
        email_input = input()
        self.email = email_input
        print("Enter your API token:")
        api_input = input()
        self.api_token = api_input
        print("Enter your organization:")
        organization_input = input()
        self.organization = organization_input.lower()
        if len(credentials_file["Email"]) == 2:
            credentials_file["Email"][0] = email_input
            credentials_file["API Token"][0] = api_input
            credentials_file["Organization"][0] = organization_input.lower()
        else:
            data = pandas.DataFrame({"Email":[email_input],"API Token":api_input,"Organization":organization_input})
            credentials_file = pandas.concat([credentials_file, data], ignore_index=True)
        credentials_file.to_csv(filepath, index=False)
        print("Credentials updated successfully.\n")
        return


menu = MainMenu()
menu.main_menu()