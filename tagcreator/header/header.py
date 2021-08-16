#!/usr/bin/env python3

import csv
import os.path
from os import path

class Header:
    def __init__(self):
        self.login_users = ["Operator", "HC", "PSI", "Supervisor", "Maintenance"]


    def features1(self):
        dict_data = []
        my_dict = {
            ":IOAccess":"",
            "Application": "ABCIP",
            "Topic": "HC",
            "AdviseActive": "Yes",
            "DDEProtocol": "No",
            "SecApplication": "",
            "SecTopic": "",
            "SecAdviseActive": "",
            "SecDDEProtocol": "",
            "FailoverExpression": "",
            "FailoverDeadband": "",
            "DFOFlag": "",
            "FBDFlag": "",
            "FailbackDeadband": ""
            }

        dict_data.append(my_dict)

        return(my_dict)


    def features(self):
        dict_data = []
        my_dict = {
            ":MemoryDisc":"",
            "Group": "$System",
            "Comment": "",
            "Logged": "No",
            "EventLogged": "No",
            "EventLoggingPriority": 0,
            "RetentiveValue": "No",
            "InitialDisc": "Off",
            "OffMsg": "",
            "OnMsg": "",
            "AlarmState": "None",
            "AlarmPri": 1,
            "AlarmComment": "",
            "AlarmAckModel": 0,
            "DSCAlarmDisable": 0,
            "DSCAlarmInhibitor": "",
            "SymbolicName": ""
            }

        dict_data.append(my_dict)

        return(my_dict)

    def access(self):
        dict_data = []
        dict1 = self.features1()
        dict1[":MemoryDisc"] = "HC"
        dict_data.append(dict1)

        return(dict_data)


    def login(self):
        dict_data = []
        for login in self.login_users:
            dict1 = self.features()
            dict1[":MemoryDisc"] = "Login_{}".format(login)
            dict_data.append(dict1)

        return(dict_data)


    def trend(self):
        dict_data = self.login()
        trend_list = ["Toggle", "ToggleBuffer"]
        for i in trend_list:
            dict1 = self.features()
            dict1[":MemoryDisc"] = "Trend{}".format(i)
            dict_data.append(dict1)

        return(dict_data)     


    def generic(self):
        dict_data = self.trend()
        generic_list = ["OffControlEnable", "TextColorLB", "TextColorRB"]
        for i in generic_list:
            dict1 = self.features()
            dict1[":MemoryDisc"] = "Generic{}".format(i)
            dict_data.append(dict1)

        return(dict_data) 


    def clean(self):
        dict_data = self.generic()
        dict1 = self.features()
        dict1[":MemoryDisc"] = "Clean_Screen"
        dict_data.append(dict1)

        return(dict_data) 


    def module_exists(self):
        file_path = "/mnt/c/Projects/ww-tag-generation/csv-files/header/header.csv"
        if path.exists(file_path):
            return True
        else:
            return False  


    def create_csv(self):
        csv_file = "header.csv"
        dict_data = self.clean()     
        csv_columns = list(dict_data[0].keys())
        
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)
        except IOError as e:
            print(e)                


if __name__ == "__main__":
    header = Header()
    header.create_csv()                 