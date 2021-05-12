#!/usr/bin/env python3

import csv

class WMDiscrete:
    def __init__(self, first_module, last_module):
        self.first_module = first_module
        self.last_module = last_module
        


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



    def hardwired_signals(self):
        dict_data = []
        signal_type = ["Infeed_Enable", "Call_For_Product", "Dump_Confirm"]
        for i in range(0, 3):
            for j in range(self.first_module, self.last_module + 1):
                dict1 = self.features()
                dict1[":IODisc"] = "WM{}_{}".format(j, signal_type[i])
                dict1["AlarmState"] = "None"
                dict1["ItemName"] = "WM{}_ModuleData.{}".format(j, signal_type[i])

                dict_data.append(dict1)

        return(dict_data)


    def weigher_comms(self):
        dict_data = self.hardwired_signals()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "WM{}_Control_Weigher_Comms".format(i)
            dict1["InitialDisc"] = "On"            
            dict1["AlarmState"] = "Off"
            dict1["ItemName"] = "WM{}_Control.Weigher_Comms".format(i)
            dict1["AlarmComment"] = "Weigher Module {} Comms Lost".format(i)

            dict_data.append(dict1)

        return(dict_data)

    def motor_fault(self):
        dict_data = self.weigher_comms()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "WM{}_Motor_Fault".format(i)
            dict1["AlarmState"] = "None"
            dict1["ItemName"] = "WM{}_Motor_Fault".format(i)
            dict1["AlarmComment"] = ""

            dict_data.append(dict1)

        return(dict_data)   

    def create_csv(self):
        csv_file = "csv-files/discrete/module_signals.csv"
        dict_data = self.motor_fault()
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
