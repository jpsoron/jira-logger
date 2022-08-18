import os
from pprint import pprint

import pandas
from jiralogger.fun import PostTimesheet, ReadTimesheet


class MainMenu:
    def __init__(self):
        self.organization = ""
        self.api_token = ""
        self.email = ""
        self.files_directory = os.path.realpath(os.path.join(os.path.dirname(__file__), '')) + "/../files/" #TODO arreglar /../
        self.timesheets = []
        self.timesheet_paths = []
        print(self.files_directory)
        return

    def main_menu(self):
        print("WELCOME TO JIRALOGGER\n-------------")
        self.read_credentials()
        while True:
            print("[1] Read timesheet\n"
                  "[2] Log timesheet to Jira\n")
            user_input = input()
            if user_input == "1":
                user_input = input("\nEnter timesheet file name:")
                self.read_timesheet(user_input)
            elif user_input == "2":
                self.print_timesheets()
                user_input = input("Enter timesheet number:")
                self.post_timesheet(int(user_input)) #TODO chequear que sea numero
            else:
                break

    def read_timesheet(self, timesheet_filename):
        timesheet_path = self.files_directory + timesheet_filename
        self.timesheet_paths.append(timesheet_path)
        self.timesheets.append(ReadTimesheet.read_timesheet(timesheet_path))
        print("Timesheet read successfully.\n")
        #TODO handle null timesheet
        return

    def post_timesheet(self, timesheet_num):
        responses = PostTimesheet.post_timesheet(self.email, self.api_token, self.organization, self.timesheets[timesheet_num-1])
        print("Timesheet P0ST successful. Log:\n")
        pprint(responses)
        i = input("Press enter to continue\n")
        #TODO validacion de codigos del request
        return

    def print_timesheets(self):
        i = 0
        timesheets_string = "\n"
        for path in self.timesheet_paths:
            i += 1
            timesheets_string += str(i) + ". " + path + "\n"
        print(timesheets_string)

    """DATA VALIDATION"""

    def read_credentials(self):
        filepath = self.files_directory + "credentials.csv"
        credentials_file = pandas.read_csv(filepath)
        self.email = self.email_validation(str(credentials_file["Email"][0]))
        self.api_token = self.api_token_validation(credentials_file["API Token"][0])
        self.organization = self.organization_validation(str(credentials_file["Organization"][0]).lower())

    def email_validation(self, email):
        if email is None:
            email = input("Enter Jira email")
        #TODO escribir mail a CSV de credenciales
        return email

    def api_token_validation(self, api_token):
        if api_token is None:
            api_token = input("Enter API token:")
        #TODO escribir token al CSV"""
        return api_token

    def organization_validation(self, organization):
        if organization is None:
            organization = input("Enter organization:")
        return organization
