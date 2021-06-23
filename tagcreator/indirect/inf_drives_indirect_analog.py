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
        self.frequencies_list = ["Max", "Min"]
        

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


    def frequencies(self):
        dict_data = []
        for freq in self.frequencies_list:
            if self.conveyor_type == "Distribution" or self.conveyor_type == "Weigher Feeder":
                dict1 = self.features()
                dict1[":IndirectAnalog"] = "GenericEngWmDs{}{}{}Freq".format(self.conveyor_type_letter, self.line, freq)
                dict_data.append(dict1)
            else:
                for i in range(self.first_vfd, self.last_vfd + 1):
                    dict1 = self.features()
                    dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}{}Freq".format(self.conveyor_type_letter, i, freq)
                    dict_data.append(dict1)

        return(dict_data)        


    def speed_ref(self):
        dict_data = self.frequencies()
        accum_speeds_list = ["Ts", "Ds"]
        mod_speeds_list = ["Hi", "Lo"]

        if self.conveyor_type == "Distribution" or self.conveyor_type == "Weigher Feeder":
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericEngWmDs{}{}".format(self.conveyor_type_letter, self.line)            
            dict_data.append(dict1)
        else:
            for i in range(self.first_vfd, self.last_vfd + 1):    
                if self.conveyor_type == "Accumulation":
                    for speed in accum_speeds_list:
                        dict1 = self.features()
                        dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}{}".format(self.conveyor_type_letter, i, speed)
                        dict_data.append(dict1)

                elif self.conveyor_type == "Modulation":
                    for speed in mod_speeds_list:
                        dict1 = self.features()
                        dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}{}".format(self.conveyor_type_letter, i, speed)
                        dict_data.append(dict1)
                    
                elif self.conveyor_type == "Transfer":
                    dict1 = self.features()
                    dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}".format(self.conveyor_type_letter, i) 
                    dict_data.append(dict1)

        return(dict_data) 


    def create_csv(self):
        csv_file = "csv-files/indirect/eng_{}_drives.csv".format(self.conveyor_type_letter)
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