#!/usr/bin/env python3

import csv
import os.path
from os import path
from indirect_analog_features import features


class RevGateIndirectAnalog:
    def __init__(self, line):
        self.line = line

        self.controls_list = ["CMD", "Faults", "ManAngle", "Status"]
        self.setpoints_list = ["MPM", "FltrWgt"]
        self.measurements_list = ["AngleSts", "LevelTrans", "ProductAvailable", "Status"]
        self.verify_list = ["BedDepth", "Hole", "PA", "PN", "Pos", "PosSp"]


    def setpoints(self):
        dict_data = []
        for setpoint in self.setpoints_list:
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericRevGate{}Sp{}".format(self.line, setpoint)
            dict_data.append(dict1)

        return(dict_data)


    def measurements(self):
        dict_data = self.setpoints()
        for measurement in self.measurements_list:
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericRevGate{}{}".format(self.line, measurement)
            dict_data.append(dict1)

        return(dict_data)     


    def verify(self):
        dict_data = self.measurements()
        for verify in self.verify_list:
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericEngRevGate{}Verify{}".format(self.line, verify)
            dict_data.append(dict1)

        return(dict_data)

    def control(self):
        dict_data = self.verify()
        for control in self.controls_list:
            dict1 = features()
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
    wm = RevGateIndirectAnalog('B')
    wm.create_csv()                 