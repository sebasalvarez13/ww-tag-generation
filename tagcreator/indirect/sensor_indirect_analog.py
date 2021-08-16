#!/usr/bin/env python3

import csv
import os.path
from os import path

class SensorIndirectAnalog:
    def __init__(self, first_sensor, last_sensor, sensor_type):
        self.first_sensor = first_sensor
        self.last_sensor = last_sensor
        self.sensor_count = (self.last_sensor + 1) - (self.first_sensor)
        
        self.sensor_type = sensor_type

        self.sensor_types = ["Analog", "Discrete"]
        self.debounce_list = ["Off", "On"]


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


    def debounce(self):
        dict_data = []
        for i in range(self.first_sensor, self.last_sensor + 1):
            for debounce in self.debounce_list:
                dict1 = self.features()
                dict1[":IndirectAnalog"] = "GenericEngSensor{}{}Db{}".format(self.sensor_type, i, debounce)
                dict_data.append(dict1)

        return(dict_data)


    def trigger(self):
        dict_data = self.debounce()
        for i in range(self.first_sensor, self.last_sensor + 1):
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericEngSensor{}{}TriggerSp".format(self.sensor_type, i)
            dict_data.append(dict1)

        return(dict_data)     


    def module_exists(self):
        file_path = "/mnt/c/Projects/ww-tag-generation/csv-files/indirect/sensor_indirect_analog.csv"
        if path.exists(file_path):
            return True
        else:
            return False  


    def create_csv(self):
        csv_file = "csv-files/indirect/sensor_indirect_analog.csv"
        if self.sensor_type == 'Analog':        
            dict_data = self.trigger()
        else:
            dict_data = self.debounce()     
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
    wm = SensorIndirectAnalog(1, 5, 'Analog')
    wm.create_csv()                 