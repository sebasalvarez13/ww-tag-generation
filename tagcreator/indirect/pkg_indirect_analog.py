#!/usr/bin/env python3

import csv
import os.path
from os import path


class PkgIndirectAnalog:
    def __init__(self, line):
        self.line = line

    
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

    def gate(self):
        dict_data = []
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericPkgWmGate{}".format(self.line)            
        dict_data.append(dict1)

        return(dict_data) 


    def gate_csw(self):
        dict_data = self.gate()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericPkgWmGate{}CSW".format(self.line)            
        dict_data.append(dict1)

        return(dict_data) 


    def csw(self):
        dict_data = self.gate_csw()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericPkgWmCSW"
        dict_data.append(dict1)

        return(dict_data)        


    def module_exists(self):
        file_path = "/mnt/c/Projects/ww-tag-generation/csv-files/indirect/pkg_indirect_analog.csv"
        if path.exists(file_path):
            return True
        else:
            return False  


    def create_csv(self):
        csv_file = "csv-files/indirect/pkg_indirect_analog.csv"
        if self.module_exists() != True :        
            dict_data = self.csw()
        else:
            dict_data = self.gate_csw()     
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
    wm = PkgIndirectAnalog('B')
    wm.create_csv()                 