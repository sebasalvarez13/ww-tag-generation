#!/usr/bin/env python3

import csv


class RVGReal:
    def __init__(self, first_gate, last_gate, line):
        line_numbers = {"A": 1, "B": 2, "C": 3, "D": 4}
        self.first_gate = first_gate
        self.last_gate = last_gate
        self.line = line
        self.line_number = line_numbers[line]


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


    def angle_manual(self):
        dict_data = []
        for i in range(self.first_gate, self.last_gate + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_RVG{}M_I_AngleManual".format(i, self.line_number)
            dict1["ItemName"] = "WM{}_RVG{}M.I_AngleManual".format(i, self.line_number)

            dict_data.append(dict1)

        return(dict_data)

    def mpm(self):
        dict_data = self.angle_manual()
        for i in range(self.first_gate, self.last_gate + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_RVG{}M_MPM".format(i, self.line_number)
            dict1["ItemName"] = "WM{}_RVG{}M.MPM".format(i, self.line_number)

            dict_data.append(dict1)

        return(dict_data)


    def angle_sts(self):
        dict_data = self.mpm()
        for i in range(self.first_gate, self.last_gate + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_RVG{}M_O_AngleSts".format(i, self.line_number)
            dict1["ItemName"] = "WM{}_RVG{}M.O_AngleSts".format(i, self.line_number)

            dict_data.append(dict1)

        return(dict_data)


    def product_available(self):
        dict_data = self.angle_sts()
        for i in range(self.first_gate, self.last_gate + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_RVG{}M_Product_Available".format(i, self.line_number)
            dict1["ItemName"] = "WM{}_RVG{}M.Product_Available".format(i, self.line_number)

            dict_data.append(dict1)

        return(dict_data)


    def position_sp(self):
        dict_data = self.product_available()
        for i in range(self.first_gate, self.last_gate + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_RVG{}MREV_Position_SP".format(i, self.line_number)
            dict1["ItemName"] = "WM{}_RVG{}MREV.Position_SP".format(i, self.line_number)

            dict_data.append(dict1)

        return(dict_data)


    def product_hole(self):
        dict_data = self.position_sp()
        for i in range(self.first_gate, self.last_gate + 1):
            dict1 = self.features()
            dict1[":IOReal"] = "WM{}_RVG{}MREV_Product_Hole".format(i, self.line_number)
            dict1["ItemName"] = "WM{}_RVG{}MREV.Product_Hole".format(i, self.line_number)

            dict_data.append(dict1)

        return(dict_data)


    def create_csv(self):
        csv_file = "csv-files/real/rvg_real_{}.csv".format(self.line)
        dict_data = self.product_hole()
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
