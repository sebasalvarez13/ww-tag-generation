#!/usr/bin/env python3

import csv


class WMReal:
    def __init__(self, first_module, last_module):
        self.first_module = first_module
        self.last_module = last_module


    def features(self):
        """Features for IO Real Tags"""
        dict_data = []
        my_dict = {
            ":IOReal":"",
            "Group": "$System",
            "Comment": "",
            "Logged": "No",
            "EventLogged": "No",
            "EventLoggingPriority": 0,
            "RetentiveValue": "No",
            "RetentiveAlarmParameters": "No",
            "AlarmValueDeadband": 0,
            "AlarmDevDeadband": 0,
            "EngUnits": "",
            "InitialValue": 0,
            "MinEU": -32768,
            "MaxEU": 32767,
            "Deadband": 0,
            "LogDeadband": 0,
            "LoLoAlarmState": "Off",
            "LoLoAlarmValue": 0,
            "LoLoAlarmPri": 1,
            "LoAlarmState": "Off",
            "LoAlarmValue": 0,
            "LoAlarmPri": 1,
            "HiAlarmState": "Off",
            "HiAlarmValue": 0,
            "HiAlarmPri": 1,
            "HiHiAlarmState":  "Off",
            "HiHiAlarmValue": 0,
            "HiHiAlarmPri": 1,
            "MinorDevAlarmState": "Off",
            "MinorDevAlarmValue": 0,
            "MinorDevAlarmPri": 1,
            "MajorDevAlarmState": "Off",
            "MajorDevAlarmValue": 0,
            "MajorDevAlarmPri": 1,
            "DevTarget": 0,
            "ROCAlarmState": "Off",
            "ROCAlarmValue": 0,
            "ROCAlarmPri": 1,
            "ROCTimeBase": "Min",
            "MinRaw": -32768,
            "MaxRaw": 32767,
            "Conversion": "Linear",
            "AccessName": "HC",
            "ItemUseTagname": "No",
            "ItemName": "",
            "ReadOnly": "No",
            "AlarmComment": "",
            "AlarmAckModel": 0,
            "LoLoAlarmDisable": 0,
            "LoAlarmDisable": 0,
            "HiAlarmDisable": 0,
            "HiHiAlarmDisable": 0,
            "MinDevAlarmDisable": 0,
            "MajDevAlarmDisable": 0,
            "RocAlarmDisable": 0,
            "LoLoAlarmInhibitor": "",
            "LoAlarmInhibitor": "",
            "HiAlarmInhibitor": "",
            "HiHiAlarmInhibitor": "",
            "MinDevAlarmInhibitor": "",
            "MajDevAlarmInhibitor": "",
            "RocAlarmInhibitor": "",
            "SymbolicName": "",
        }

        dict_data.append(my_dict)

        return(my_dict)


    def bag_speed(self):
        dict_data = []
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_Bag_Speed".format(i)
            dict1["ItemName"] = "WM{}_ModuleData.BagSpeed".format(i)

            dict_data.append(dict1)

        return(dict_data)

    def bag_weight(self):
        dict_data = self.bag_speed()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_Bag_Weight".format(i)
            dict1["ItemName"] = "WM{}_ModuleData.BagWeight".format(i)

            dict_data.append(dict1)

        return(dict_data)


    def oit_bagspeed_target(self):
        dict_data = self.bag_weight()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_Control_OIT_BagSpeed".format(i)
            dict1["ItemName"] = "WM{}_Control.OIT_BagSpeed".format(i)

            dict_data.append(dict1)

        return(dict_data)


    def oit_bagweight_target(self):
        dict_data = self.oit_bagspeed_target()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_Control_OIT_BagWeight".format(i)
            dict1["ItemName"] = "WM{}_Control.OIT_BagWeight".format(i)

            dict_data.append(dict1)

        return(dict_data)


    def product_needed_raw(self):
        dict_data = self.oit_bagweight_target()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_ProductNeeded_Raw".format(i)
            dict1["ItemName"] = "WM{}_ModuleData.ProductNeeded_Raw".format(i)

            dict_data.append(dict1)

        return(dict_data)


    def create_csv(self):
        csv_file = "csv-files/real/wm_real.csv"
        dict_data = self.product_needed_raw()
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
    wm = WMReal(1,5)
    wm.create_csv()
