#!/usr/bin/env python3

import csv

class VFDDiscrete:
    def __init__(self, first_vfd, last_vfd, conveyor_type, line):
        conveyor_types = {"Distribution": "D", "Transfer": "T", "Accumulation": "A", "Weigher Feeder": "WF", "Modulation": "XF"}
        self.first_vfd = first_vfd
        self.last_vfd = last_vfd
        self.conveyor_type = conveyor_type
        self.conveyor_type_letter = conveyor_types[conveyor_type]
        self.line = line

        if self.conveyor_type == "Weigher Feeder":
            self.line = ""

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

    def disconnect(self):
        dict_data = []
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "M{}{}{}_Disconnect".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmState"] = "Off"
            dict1["ItemName"] = "M{}{}{}.Disconnect".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmComment"] = "{} Conveyor {}{} Disconnected".format(self.conveyor_type, i, self.line)

            dict_data.append(dict1)

        return(dict_data)


    def fault_disconnect(self):
        dict_data = self.disconnect()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "M{}{}{}_Fault_Disconnect".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmState"] = "On"
            dict1["ItemName"] = "M{}{}{}_Faults.Disconnect".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmComment"] = "{} Conveyor {}{} Fault Disconnect".format(self.conveyor_type, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def fault_communication(self):
        dict_data = self.fault_disconnect()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "M{}{}{}_Fault_Communication".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmState"] = "On"
            dict1["ItemName"] = "M{}{}{}_Faults.Communication".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmComment"] = "{} Conveyor {}{} Fault Communication".format(self.conveyor_type, i, self.line)

            dict_data.append(dict1)

        return(dict_data)


    def fault_device(self):
        dict_data = self.fault_communication()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "M{}{}{}_Fault_Device".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmState"] = "On"
            dict1["ItemName"] = "M{}{}{}_Faults.Device".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmComment"] = "{} Conveyor {}{} Fault Device".format(self.conveyor_type, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def fault_ready(self):
        dict_data = self.fault_device()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "M{}{}{}_Fault_Ready".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmState"] = "On"
            dict1["ItemName"] = "M{}{}{}_Faults.Ready".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmComment"] = "{} Conveyor {}{} Fault Ready".format(self.conveyor_type, i, self.line)

            dict_data.append(dict1)

        return(dict_data)

    def fault_failed_forward(self):
        dict_data = self.fault_ready()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "M{}{}{}_Fault_FailedForward".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmState"] = "On"
            dict1["ItemName"] = "M{}{}{}_Faults.FailedForward".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmComment"] = "{} Conveyor {}{} Fault Failed Forward".format(self.conveyor_type, i, self.line)

            dict_data.append(dict1)

        return(dict_data)


    def fault(self):
        dict_data = self.fault_failed_forward()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IODisc"] = "M{}{}{}_Fault".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmState"] = "On"
            dict1["ItemName"] = "M{}{}{}.Fault".format(self.conveyor_type_letter, i, self.line)
            dict1["AlarmComment"] = "{} Conveyor {}{} Faulted".format(self.conveyor_type, i, self.line)

            dict_data.append(dict1)

        return(dict_data)


    def create_csv(self):
        csv_file = "csv-files/discrete/vfd_discrete_{}_{}.csv".format(self.conveyor_type, self.line)
        dict_data = self.fault()
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
    wm = VFDFaults()
    #dict_data = hardwired_signals(10, 22)

