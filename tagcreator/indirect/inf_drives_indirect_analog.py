#!/usr/bin/env python3

import csv

class InfDrivesIndirectAnalog:
    def __init__(self, first_vfd, last_vfd, conveyor_type, line):
        conveyor_types = {"Transfer": "Trans", "Accumulation": "Accum", "Modulation": "Mod", "Distribution": "Dist", "Weigher Feeder": "WF"}
        self.first_vfd = first_vfd
        self.last_vfd = last_vfd
        self.conveyor_type = conveyor_type
        self.conveyor_type_letter = conveyor_types[conveyor_type]
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


    def max_freq(self):
        dict_data = []
        if self.conveyor_type == "Distribution" or self.conveyor_type == "Weigher Feeder":
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}MaxFreq".format(self.conveyor_type_letter, self.line)
            dict_data.append(dict1)
        else:
            for i in range(self.first_vfd, self.last_vfd + 1):
                dict1 = self.features()
                dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}MaxFreq".format(self.conveyor_type_letter, i)
                dict_data.append(dict1)

        return(dict_data)        


    def min_freq(self):
        dict_data = self.max_freq()
        if self.conveyor_type == "Distribution" or self.conveyor_type == "Weigher Feeder":
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}MinFreq".format(self.conveyor_type_letter, self.line)
            dict_data.append(dict1)
        else:
            for i in range(self.first_vfd, self.last_vfd + 1):
                dict1 = self.features()
                dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}MinFreq".format(self.conveyor_type_letter, i)
                dict_data.append(dict1)

        return(dict_data)            


    def speed_ref(self):
        dict_data = self.min_freq()
        accum_speeds_list = ["Ts", "Ds"]
        mod_speeds_list = ["Hi", "Lo"]
     
        if self.conveyor_type == "Accumulation":
            for i in range(self.first_vfd, self.last_vfd + 1):
                for j in accum_speeds_list:
                    dict1 = self.features()
                    dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}{}".format(self.conveyor_type_letter, i, j)
                    dict_data.append(dict1)

        elif self.conveyor_type == "Modulation":
            for i in range(self.first_vfd, self.last_vfd + 1):
                for j in mod_speeds_list:
                    dict1 = self.features()
                    dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}{}".format(self.conveyor_type_letter, i, j)
                    dict_data.append(dict1)
               
        elif self.conveyor_type == "Transfer":
            for i in range(self.first_vfd, self.last_vfd + 1):
                dict1 = self.features()
                dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}".format(self.conveyor_type_letter, i) 
                dict_data.append(dict1)

        else:
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}".format(self.conveyor_type_letter, self.line)            
            dict_data.append(dict1)

        return(dict_data) 


    def create_csv(self):
        csv_file = "csv-files/indirect/infeed_{}_drives.csv".format(self.conveyor_type_letter)
        dict_data = self.speed_ref()
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
    wm = InfDrivesIndirectAnalog(1, 4, "Distribution", 'A')
    wm.create_csv()                 