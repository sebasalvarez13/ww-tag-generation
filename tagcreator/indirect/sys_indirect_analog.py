#!/usr/bin/env python3

import csv
import os.path
from os import path
from tagcreator.indirect.indirect_analog_features import features

class SysIndirectAnalog:
    def __init__(self):
        self.tag_start = "GenericSys"
        self.system_products = ["Available", "Needed", "Recirc"]


    def mod_speed(self):
        dict_data = []
        dict1 = features()
        dict1[":IndirectAnalog"] = "{}ModulatingSpeed".format(self.tag_start)            
        dict_data.append(dict1)

        return(dict_data) 


    def product(self):
        dict_data = self.mod_speed()
        for product in self.system_products:
            dict1 = features()
            dict1[":IndirectAnalog"] = "{}Product{}".format(self.tag_start, product)
            dict_data.append(dict1)

        return(dict_data)        


    def module_exists(self):
        file_path = "/mnt/c/Projects/ww-tag-generation/csv-files/indirect/sys_indirect_analog.csv"
        if path.exists(file_path):
            return True
        else:
            return False  


    def create_csv(self):
        csv_file = "csv-files/indirect/sys_indirect_analog.csv"
        dict_data = self.product()     
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
    wm = SysIndirectAnalog()
    wm.create_csv()                 