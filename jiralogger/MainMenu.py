from jiralogger.fun import PostTimesheet, ReadTimesheet
import os
from pprint import pprint
from inspect import getsourcefile
from os.path import abspath

import pandas



class MainMenu:
    def __init__(self):
        self.organization = ""
        self.api_token = ""
        self.email = ""
        current_file_path = abspath(getsourcefile(lambda:0))
        self.files_directory = current_file_path[:-11] + "..\\files\\"
        self.timesheets = []
        self.timesheet_paths = []
        return

    def main_menu(self):
        print("WELCOME TO JIRALOGGER\n-------------")
        self.read_credentials()
        while True:
            print("[1] Read timesheet\n"
                  "[2] Log timesheet to Jira\n"
                  "[3] Update credentials\n"
                  )
            user_input = input()
            if user_input == "1":
                user_input = input("\nEnter timesheet file name:")
                self.read_timesheet(user_input)
            elif user_input == "2":
                self.print_timesheets()
                user_input = input("Enter timesheet number:")
                self.post_timesheet(int(user_input)) #TODO chequear que sea numero
            elif user_input == "3":
                self.update_credentials()
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

    def read_credentials(self):
        filepath = self.files_directory + "credentials.csv"
        credentials_file = pandas.read_csv(filepath)

        if len(credentials_file["Email"]) > 1:
            self.email = str(credentials_file["Email"][0])
            self.api_token = str(credentials_file["API Token"][0])
            self.organization = str(credentials_file["Organization"][0])
        else:
            print("API credentials are empty. Please fill them out below: ")
            self.update_credentials()

    def update_credentials(self):
        filepath = self.files_directory + "credentials.csv"
        credentials_file = pandas.read_csv(filepath)
        print("Enter your email:")
        email_input = input()
        self.email = email_input
        print("Enter your API token:")
        api_input = input()
        self.api_token = api_input
        print("Enter your organization:")
        organization_input = input()
        self.organization = organization_input
        if len(credentials_file["Email"]) == 2:
            credentials_file["Email"][0] = email_input
            credentials_file["API Token"][0] = api_input
            credentials_file["Organization"][0] = organization_input
        else:
            data = pandas.DataFrame({"Email":[email_input],"API Token":api_input,"Organization":organization_input})
            credentials_file = pandas.concat([credentials_file, data], ignore_index=True)
        credentials_file.to_csv(filepath, index=False)
        print("Credentials updated successfully.\n")
        return


menu = MainMenu()
menu.main_menu()