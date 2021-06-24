#!/usr/bin/env python3

import csv
import os.path
from os import path

class RevGateIndirectAnalog:
    def __init__(self, first_gate, last_gate, line):
        self.first_gate = first_gate
        self.last_gate = last_gate
    
        self.line = line

        self.controls_list = ["CMD", "Faults", "ManAngle", "Status"]
        self.setpoints_list = ["MPM", "FltrWgt"]
        self.measurements_list = ["AngleSts", "LevelTrans", "ProductAvailable", "Status"]
        self.verify_list = ["BedDepth", "Hole", "PA", "PN", "Pos", "PosSp"]

    def features(self):
        dict_data = []
        my_dict = {
            ":IndirectAnalog":"",
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


    def setpoints(self):
        dict_data = []
        for setpoint in self.setpoints_list:
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericRevGate{}Sp{}".format(self.line, setpoint)
            dict_data.append(dict1)

        return(dict_data)


    def measurements(self):
        dict_data = self.setpoints()
        for measurement in self.measurements_list:
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericRevGate{}{}".format(self.line, measurement)
            dict_data.append(dict1)

        return(dict_data)     


    def verify(self):
        dict_data = self.measurements()
        for verify in self.verify_list:
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericEngRevGate{}Verify{}".format(self.line, verify)
            dict_data.append(dict1)

        return(dict_data)

    def control(self):
        dict_data = self.verify()
        for control in self.controls_list:
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericRevGateControl{}".format(control)
            dict_data.append(dict1)

        return(dict_data)
         


    def module_exists(self):
        file_path = "/mnt/c/Projects/ww-tag-generation/csv-files/indirect/rvg.csv"
        if path.exists(file_path):
            return True
        else:
            return False  


    def create_csv(self):
        csv_file = "csv-files/indirect/rvg.csv"
        if self.module_exists() != True :        
            dict_data = self.control()
        else:
            dict_data = self.verify()     
        csv_columns = list(dict_data[0].keys())
        
        try:
            with open(csv_file, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                if self.module_exists() != True:
                    writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)
        except IOError as e:
            print(e)  


if __name__ == "__main__":
    wm = RevGateIndirectAnalog(1, 5, 'B')
    wm.create_csv()                 