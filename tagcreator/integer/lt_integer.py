#!/usr/bin/env python3

import csv
#from website_example import first_transmitter, last_transmitter, gate_num, line

class LTInteger:
    def __init__(self, first_transmitter, last_transmitter, transmitter_number, conveyor_type, line):
        conveyor_types = {"Distribution": "D", "Transfer": "T", "Accumulation": "A", "Weigher Feeder": "WF", "Modulation": "X"}
        self.first_transmitter = first_transmitter
        self.last_transmitter = last_transmitter
        self.transmitter_number = transmitter_number
        self.conveyor_type = conveyor_type
        self.conveyor_type_letter = conveyor_types[conveyor_type]
        self.line = line


    def features(self):
        """Features for IO Integer Tags"""
        dict_data = []
        my_dict = {
            ":IOInt":"",
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


    def setpoint(self):
        dict_data = []
        for i in range(self.first_transmitter, self.last_transmitter + 1):
            dict1 = self.features()
            dict1[":IOInt"] = "LT{}{}{}{}_DB_SP".format(self.transmitter_number, self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "LT{}{}{}{}_DB_SP".format(self.transmitter_number, self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def debounce_on_pre(self):
        dict_data = self.setpoint()
        for i in range(self.first_transmitter, self.last_transmitter + 1):
            dict1 = self.features()
            dict1[":IOInt"] = "LT{}{}{}{}_DB_Debounce_On_Pre".format(self.transmitter_number, self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "LT{}{}{}{}_DB_Debounce_On.Pre".format(self.transmitter_number, self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def debounce_off_pre(self):
        dict_data = self.debounce_on_pre()
        for i in range(self.first_transmitter, self.last_transmitter + 1):
            dict1 = self.features()
            dict1[":IOInt"] = "LT{}{}{}{}_DB_Debounce_Off_Pre".format(self.transmitter_number, self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "LT{}{}{}{}_DB_Debounce_Off.Pre".format(self.transmitter_number, self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def create_csv(self):
        csv_file = "csv-files/integer/lt_integer_{}_{}.csv".format(self.conveyor_type, self.line)
        dict_data = self.debounce_off_pre()
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
    wm = LTInteger(3, 5, 1, "Distribution", "A")
    #print(first_module, last_module, gate_num, line)
    wm.create_csv()
