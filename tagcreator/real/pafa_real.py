#!/usr/bin/env python3

import csv


class PAFAReal:
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


    def pafa_cv(self):
        dict_data = []
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_PAFA_CV".format(i)
            dict1["ItemName"] = "WM{}_OuterLoopPID.CV".format(i)
            dict1["Logged"] = "Yes"
            dict1["MaxEU"] = 100
            dict1["MaxRaw"] = 100

            dict_data.append(dict1)

        return(dict_data)

    
    def pafa_pv(self):
        dict_data = self.pafa_cv()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_PAFA_PV".format(i)
            dict1["ItemName"] = "WM{}_PAFA.PID_PV".format(i)
            dict1["Logged"] = "Yes"
            dict1["MaxEU"] = 2
            dict1["MaxRaw"] = 2

            dict_data.append(dict1)

        return(dict_data)


    def wf_trend(self):
        dict_data = self.pafa_pv()
        for i in range(self.first_module, self.last_module + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_WF_Trend".format(i)
            dict1["ItemName"] = "WM{}_WF_Trend".format(i)
            dict1["Logged"] = "Yes"
            dict1["MaxEU"] = 2
            dict1["MaxRaw"] = 2

            dict_data.append(dict1)

        return(dict_data)


    def create_csv(self):
        csv_file = "csv-files/real/pafa_real{}.csv"
        dict_data = self.wf_trend()
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
    rvg = RVGReal(3, 5, "A")
    #print(first_module, last_module, gate_num, line)
    rvg.create_csv()
