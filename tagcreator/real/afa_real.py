#!/usr/bin/env python3

import csv


class AFAReal:
    def __init__(self, line):
        self.line = line
        self.derated_list = ["Coarse", "Fine", "Medium", "No"]


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


    def adjust_amount(self):
        dict_data = []
        for adjust in self.derated_list[0:3]:
            dict1 = self.features()
            dict1[":IOReal"] = "Line{}_AFA_{}_Adjust_Amount".format(self.line, adjust)
            dict1["ItemName"] = "Line{}_AFA.{}_Adjust_Amount".format(self.line, adjust)

            dict_data.append(dict1)

        return(dict_data)


    def neg_limit(self):
        dict_data = self.adjust_amount() 
        for adjust in self.derated_list:
            dict1 = self.features()
            dict1[":IOReal"] = "Line{}_AFA_{}_Neg_Lmt".format(self.line, adjust)
            dict1["ItemName"] = "Line{}_AFA.{}_Neg_Limit".format(self.line, adjust)

            dict_data.append(dict1)

        return(dict_data)


    def pos_limit(self):
        dict_data = self.neg_limit() 
        for adjust in self.derated_list:
            dict1 = self.features()
            dict1[":IOReal"] = "Line{}_AFA_{}_Pos_Lmt".format(self.line, adjust)
            dict1["ItemName"] = "Line{}_AFA.{}_Pos_Limit".format(self.line, adjust)

            dict_data.append(dict1)

        return(dict_data)


    def cv(self):
        dict_data = self.pos_limit()
        dict1 = self.features()
        dict1[":IOReal"] = "Line{}_AFA_CV".format(self.line)
        dict1["ItemName"] = "Line{}_AFA_PID.CV".format(self.line)
        dict1["MaxEU"] = 100
        dict1["MinEU"] = 0
        dict1["MaxRaw"] = 100
        dict1["MinRaw"] = 0

        dict_data.append(dict1)

        return(dict_data)


    def cv_trend(self):
        dict_data = self.cv()
        dict1 = self.features()
        dict1[":IOReal"] = "Line{}_AFA_CV_TREND".format(self.line)
        dict1["ItemName"] = "InfeedLine{}_PID_CV_TREND.Value".format(self.line)
        dict1["Logged"] = "Yes"
        dict1["MaxEU"] = 100
        dict1["MinEU"] = 0
        dict1["MaxRaw"] = 100
        dict1["MinRaw"] = 0

        dict_data.append(dict1)

        return(dict_data)


    def create_csv(self):
        csv_file = "csv-files/real/afa_real_{}.csv".format(self.line)
        dict_data = self.cv_trend()
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
    afa = AFAReal("A")
    afa.create_csv()
