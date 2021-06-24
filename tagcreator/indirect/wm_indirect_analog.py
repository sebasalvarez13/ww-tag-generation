#!/usr/bin/env python3

import csv
import os.path
from os import path


class WMIndirectAnalog:
    def __init__(self, conveyor_type, line):
        conveyor_types_dict = {"Distribution": ["D", "Dist"], "Transfer": ["T", "Trans"], "Accumulation": ["A", "Accum"], "Weigher Feeder": ["WF", "WF"], "Modulation": ["XF", "Mod"]}

        self.conveyor_type = conveyor_type
        self.conveyor_type_letter = conveyor_types_dict[conveyor_type][0]
        self.conveyor_type_short = conveyor_types_dict[conveyor_type][1]
    
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

    def drives(self):
        dict_data = []
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "Generic{}{}CSW".format(self.conveyor_type_short, self.line)            
        dict_data.append(dict1)

        return(dict_data) 


    def bag_speed(self):
        dict_data = self.drives()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericBagSpeedEntry"
        dict_data.append(dict1)

        return(dict_data)        


    def bag_weight(self):
        dict_data = self.bag_speed()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericBagWeightEntry"
        dict_data.append(dict1)

        return(dict_data) 


    def control(self):
        dict_data = self.bag_weight()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericControlCSW"           
        dict_data.append(dict1)

        return(dict_data) 


    def control_disable(self):
        dict_data = self.control()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericControlDisableCSW"           
        dict_data.append(dict1)

        return(dict_data) 


    def suspension_timer(self):
        dict_data = self.control_disable()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericEngWmSp_SuspensionTimer"           
        dict_data.append(dict1)

        return(dict_data) 

    def line_select(self):
        dict_data = self.suspension_timer()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericLineSelect"           
        dict_data.append(dict1)

        return(dict_data) 


    def weigher_control(self):
        dict_data = self.line_select()
        dict1 = self.features()
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
        if self.module_exists() != True :        
            dict_data = self.weigher_control()
        else:
            dict_data = self.drives()     
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
    wm = WMIndirectAnalog("Distribution", 'A')
    wm.create_csv()                 