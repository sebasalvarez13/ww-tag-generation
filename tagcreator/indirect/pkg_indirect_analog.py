#!/usr/bin/env python3

import csv
import os.path
from os import path
from tagcreator.indirect.indirect_analog_features import features


class PkgIndirectAnalog:
    def __init__(self, line):
        self.line = line


    def gate(self):
        dict_data = []
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericPkgWmGate{}".format(self.line)            
        dict_data.append(dict1)

        return(dict_data) 


    def gate_csw(self):
        dict_data = self.gate()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericPkgWmGate{}CSW".format(self.line)            
        dict_data.append(dict1)

        return(dict_data) 


    def csw(self):
        dict_data = self.gate_csw()
        dict1 = features()
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
        
        if self.module_exists() != True:
            try:
                with open(csv_file, 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for data in dict_data:
                        writer.writerow(data)
            except IOError as e:
                print(e)
        else:
            try:
                with open(csv_file, 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    #writer.writeheader()
                    for data in dict_data:
                        writer.writerow(data)
            except IOError as e:
                print(e)                           

if __name__ == "__main__":
    wm = PkgIndirectAnalog('B')
    wm.create_csv()                 