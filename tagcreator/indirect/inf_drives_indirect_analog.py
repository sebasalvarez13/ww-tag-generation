#!/usr/bin/env python3

import csv

class InfDrivesIndirectAnalog:
    def __init__(self, first_vfd, last_vfd, conveyor_type, line):
        conveyor_types = {"Transfer": "Trans", "Accumulation": "Accum", "Modulation": "Mod"}
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


    def max_freq(self):
        dict_data = []
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}MaxFreq".format(self.conveyor_type_letter, i)

            dict_data.append(dict1)

        return(dict_data)        

    def min_freq(self):
        dict_data = self.max_freq()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}MinFreq".format(self.conveyor_type_letter, i)

            dict_data.append(dict1)

        return(dict_data)  


    def transfer(self):
        dict_data = self.min_freq()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}Ts".format(self.conveyor_type_letter, i)

            dict_data.append(dict1)

        return(dict_data)                 


    def discharge(self):
        dict_data = self.transfer()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}Ds".format(self.conveyor_type_letter, i)

            dict_data.append(dict1)

        return(dict_data)          