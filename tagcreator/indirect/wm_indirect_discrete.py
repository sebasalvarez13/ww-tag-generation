#!/usr/bin/env python3

import csv

class WMIndirectDiscrete:
    def __init__(self):
        self.lines = ["A", "B", "C", "D"]
        

    def features(self):
        dict_data = []
        my_dict = {
            ":IndirectDisc":"",
            "Group": "$System",
            "Comment": "",
            "Logged": "No",
            "EventLogged": "No",
            "EventLoggingPriority": 0,
            "RetentiveValue": "No",
            "SymbolicName": ""
            }

        dict_data.append(my_dict)

        return(my_dict)


    def hardwired_signals(self):
        dict_data = []
        signal_type = ["InfeedEnable", "CallForProduct"]
        for i in range(0, 2):
            dict1 = self.features()
            dict1[":IndirectDisc"] = "Generic{}".format(signal_type[i])
            dict_data.append(dict1)

        return(dict_data)


    def weigher_comms(self):
        dict_data = self.hardwired_signals()
        dict1 = self.features()
        dict1[":IndirectDisc"] = "GenericWeigherComms"
        dict_data.append(dict1)

        return(dict_data)
   

    def perm_estop(self):
        dict_data = self.weigher_comms()
        dict1 = self.features()
        dict1[":IndirectDisc"] = "GenericPermEstop"
        dict_data.append(dict1)

        return(dict_data)    


    def perm_motor_fault(self):
        dict_data = self.perm_estop()
        dict1 = self.features()
        dict1[":IndirectDisc"] = "GenericPermMotorFault"
        dict_data.append(dict1)

        return(dict_data)


    def line_sel_mode(self):
        dict_data = self.perm_motor_fault()
        for i in self.lines:
            dict1 = self.features()
            dict1[":IndirectDisc"] = "GenericLine{}SelMode".format(i)
            dict_data.append(dict1)

        return(dict_data)          


    def create_csv(self):
        csv_file = "csv-files/discrete/wm_indirect.csv"
        dict_data = self.line_sel_mode()
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
    wm = WMIndirectDiscrete()
    wm.create_csv()
