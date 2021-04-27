#!/usr/bin/env python3

import csv

class PAFADiscrete:
    def __init__(self, first_module, last_module):
        self.first_module = first_module
        self.last_module = last_module
        #self.create_csv()


    def features(self):
        dict_data = []
        my_dict = {
            ":IODisc":"",
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
            "DConversion": "Direct",
            "AccessName": "HC",
            "ItemUseTagname": "No",
            "ItemName": "",
            "ReadOnly": "No",
            "AlarmComment": "",
            "AlarmAckModel": 0,
            "DSCAlarmDisable": 0,
            "DSCAlarmInhibitor": "",
            "SymbolicName": ""
            }

        dict_data.append(my_dict)

        return(my_dict)


    def permissive(self):
        dict_data = []
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "WM{}_PAFA_Permissive".format(i)
            dict1["AlarmState"] = "None"
            dict1["ItemName"] = "WM{}_PAFA.Permissive_PAFA".format(i)

            dict_data.append(dict1)

        return(dict_data)
        

    def suspended(self):
        dict_data = self.permissive()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "WM{}_PAFA_Suspended".format(i)
            dict1["AlarmState"] = "None"
            dict1["ItemName"] = "WM{}_ModuleFlow.Permissive_Unsuspend".format(i)

            dict_data.append(dict1)

        return(dict_data)   


    def green_efficiency(self):
        dict_data = self.suspended()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "WM{}_PAFA_Green".format(i)
            dict1["AlarmState"] = "None"
            dict1["ItemName"] = "WM{}_PAFA.Efficiency_Green".format(i)

            dict_data.append(dict1)

        return(dict_data)


    def yellow_efficiency(self):
        dict_data = self.green_efficiency()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "WM{}_PAFA_Yellow".format(i)
            dict1["AlarmState"] = "None"
            dict1["ItemName"] = "WM{}_PAFA.Efficiency_Yellow".format(i)

            dict_data.append(dict1)

        return(dict_data)


    def red_efficiency(self):
        dict_data = self.yellow_efficiency()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "WM{}_PAFA_Red".format(i)
            dict1["AlarmState"] = "None"
            dict1["ItemName"] = "WM{}_PAFA.Efficiency_Red".format(i)

            dict_data.append(dict1)

        return(dict_data)                


    def create_csv(self):
        csv_file = "csv-files/discrete/pafa_discrete.csv"
        dict_data = self.red_efficiency()
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
    wm = WeigherModule()
