#!/usr/bin/env python3

import csv
#from website_example import first_gate, last_gate, gate_num, line

class SGDiscrete:
    def __init__(self, first_gate, last_gate, gate_number, conveyor_type, line):
        conveyor_types = {"Distribution": "D", "Transfer": "T", "Accumulation": "A", "Weigher Feeder": "WF", "Modulation": "X"}
        self.first_gate = first_gate
        self.last_gate = last_gate
        self.gate_number = gate_number
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



    def auto_pb(self):
        dict_data = []
        for i in range(self.first_gate, self.last_gate + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "YSG{}M{}{}{}_Auto_PB".format(self.gate_number, self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "YSG{}M{}{}{}.AutoPB".format(self.gate_number, self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def manual_mode(self):
        dict_data = self.auto_pb()
        for i in range(self.first_gate, self.last_gate + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "YSG{}M{}{}{}_Manual_Mode".format(self.gate_number, self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "YSG{}M{}{}{}.ManualMode".format(self.gate_number, self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def manual_close(self):
        dict_data = self.manual_mode()
        for i in range(self.first_gate, self.last_gate + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "YSG{}M{}{}{}_Manual_Close".format(self.gate_number, self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "YSG{}M{}{}{}.ManualClose".format(self.gate_number, self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def manual_open(self):
        dict_data = self.manual_close()
        for i in range(self.first_gate, self.last_gate + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "YSG{}M{}{}{}_Manual_Open".format(self.gate_number, self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "YSG{}M{}{}{}.ManualOpen".format(self.gate_number, self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def open(self):
        dict_data = self.manual_open()
        for i in range(self.first_gate, self.last_gate + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "YSG{}M{}{}{}_Open".format(self.gate_number, self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "YSG{}M{}{}{}.Open".format(self.gate_number, self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def create_tags(self):
        dict_data = self.stat_off()

        return(dict_data)
        
    def create_csv(self):
        csv_file = "csv-files/discrete/slide_gates_{}_{}.csv".format(self.conveyor_type, self.line)
        dict_data = self.open()
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
    sg = SGDiscrete(1, 5, 1, "Distribution", "C")
    sg.create_csv()
