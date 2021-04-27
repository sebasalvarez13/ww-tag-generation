#!/usr/bin/env python3

import csv


class WMStatsReal:
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
            "MinEU": 0,
            "MaxEU": 100,
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
            "MinRaw": 0,
            "MaxRaw": 100,
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


    def module_m(self):
        dict_data = []
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_Module_M".format(i)
            dict1["ItemName"] = "WM{}_ModuleFlow.Module_M".format(i)
            dict1["MinRaw"] = -32768
            dict1["MaxRaw"] = 32767
            dict1["MinEU"] = -32768
            dict1["MaxEU"] = 32767

            dict_data.append(dict1)

        return(dict_data)


    def bpm(self):
        dict_data = self.module_m()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_ModuleStats_BPM".format(i)
            dict1["ItemName"] = "WM{}_ModuleStats.StatsBagsPerMinute".format(i)
            dict1["MinRaw"] = -32768
            dict1["MaxRaw"] = 32767
            dict1["MinEU"] = -32768
            dict1["MaxEU"] = 32767

            dict_data.append(dict1)

        return(dict_data)


    def bpm_decimal(self):
        dict_data = self.bpm()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_ModuleStats_BPM_Decimal".format(i)
            dict1["ItemName"] = "WM{}_ModuleStats.StatsAFABagsPerMinute".format(i)
            dict1["MinRaw"] = 0
            dict1["MaxRaw"] = 1
            dict1["MinEU"] = 0
            dict1["MaxEU"] = 1
            dict1["Logged"] = "Yes"

            dict_data.append(dict1)

        return(dict_data)


    def bpm_percent(self):
        dict_data = self.bpm_decimal()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_ModuleStats_BPM_Percent".format(i)
            dict1["ItemName"] = "WM{}_ModuleStats.StatsAFABagsPerMinutePercent".format(i)
            dict1["MinRaw"] = 0
            dict1["MaxRaw"] = 100
            dict1["MinEU"] = 0
            dict1["MaxEU"] = 100
            dict1["Logged"] = "Yes"

            dict_data.append(dict1)

        return(dict_data)



    def dc_decimal(self):
        dict_data = self.bpm_percent()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_ModuleStats_DC_Decimal".format(i)
            dict1["ItemName"] = "WM{}_ModuleStats.StatsDutyCycle".format(i)
            dict1["MinRaw"] = 0
            dict1["MaxRaw"] = 1
            dict1["MinEU"] = 0
            dict1["MaxEU"] = 1
            dict1["Logged"] = "Yes"

            dict_data.append(dict1)

        return(dict_data)


    def dc_percent(self):
        dict_data = self.dc_decimal()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_ModuleStats_DC_Percent".format(i)
            dict1["ItemName"] = "WM{}_ModuleStats.StatsDutyCycle".format(i)
            dict1["MinRaw"] = 0
            dict1["MaxRaw"] = 100
            dict1["MinEU"] = 0
            dict1["MaxEU"] = 100
            dict1["Logged"] = "Yes"

            dict_data.append(dict1)

        return(dict_data)


    def create_csv(self):
        csv_file = "csv-files/real/wmstats_real.csv"
        dict_data = self.dc_percent()
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
    pr = WMStatsReal(1, 5)
    #print(first_module, last_module, gate_num, line)
    pr.create_csv()
