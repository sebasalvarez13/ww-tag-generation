#!/usr/bin/env python3

import csv
import os.path
from os import path
from tagcreator.indirect.indirect_analog_features import features



class WMIndirectAnalog:
    def __init__(self):
        pass 


    def bag_speed(self):
        dict_data = []
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericBagSpeedEntry"
        dict_data.append(dict1)

        return(dict_data)        


    def bag_weight(self):
        dict_data = self.bag_speed()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericBagWeightEntry"
        dict_data.append(dict1)

        return(dict_data) 


    def control(self):
        dict_data = self.bag_weight()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericControlCSW"           
        dict_data.append(dict1)

        return(dict_data) 


    def control_disable(self):
        dict_data = self.control()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericControlDisableCSW"           
        dict_data.append(dict1)

        return(dict_data) 


    def suspension_timer(self):
        dict_data = self.control_disable()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericEngWmSp_SuspensionTimer"           
        dict_data.append(dict1)

        return(dict_data) 

    def line_select(self):
        dict_data = self.suspension_timer()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericLineSelect"           
        dict_data.append(dict1)

        return(dict_data) 


    def weigher_control(self):
        dict_data = self.line_select()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericWeigherControlPkg"           
        dict_data.append(dict1)

        return(dict_data) 


    def module_exists(self):
        file_path = "/mnt/c/Projects/ww-tag-generation/csv-files/indirect/wm_indirect_analog.csv"
        if path.exists(file_path):
            return True
        else:
            return False  


    def create_csv(self):
        csv_file = "csv-files/indirect/wm_indirect_analog.csv"       
        dict_data = self.weigher_control()
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
    wm = WMIndirectAnalog()
    wm.create_csv()                 