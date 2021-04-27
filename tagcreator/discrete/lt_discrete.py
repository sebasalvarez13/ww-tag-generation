#!/usr/bin/env python3

import csv
#from website_example import first_transmitter, last_transmitter, gate_num, line

class LTDiscrete:
    def __init__(self, first_transmitter, last_transmitter, transmitter_number, conveyor_type, line):
        conveyor_types = {"Distribution": "D", "Transfer": "T", "Accumulation": "A", "Weigher Feeder": "WF", "Modulation": "X"}
        self.first_transmitter = first_transmitter
        self.last_transmitter = last_transmitter
        self.transmitter_number = transmitter_number
        self.conveyor_type = conveyor_type
        self.conveyor_type_letter = conveyor_types[conveyor_type]
        self.line = line


    def features(self):
        """Features for IO Discrete Tags"""
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



    def stat_on(self):
        dict_data = []
        for i in range(self.first_transmitter, self.last_transmitter + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "LT{}{}{}{}_DB_Stat_On".format(self.transmitter_number, self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "LT{}{}{}{}_DB.Stat_On".format(self.transmitter_number, self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def stat_off(self):
        dict_data = self.stat_on()
        for i in range(self.first_transmitter, self.last_transmitter + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "LT{}{}{}{}_DB_Stat_Off".format(self.transmitter_number, self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "LT{}{}{}{}_DB.Stat_Off".format(self.transmitter_number, self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def create_tags(self):
        dict_data = self.stat_off()

        return(dict_data)
        
    def create_csv(self):
        csv_file = "csv-files/discrete/lt_discrete_{}_{}.csv".format(self.conveyor_type, self.line)
        dict_data = self.stat_off()
        csv_columns = list(dict_data[0].keys())

        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)
        except IOError:
            print("I/O error")

if __name__ == "__main__":
    wm = LTDiscrete()
