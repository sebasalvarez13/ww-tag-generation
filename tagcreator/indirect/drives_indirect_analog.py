#!/usr/bin/env python3

import csv
from tagcreator.indirect.indirect_analog_features import features


class DrivesIndirectAnalog:
    def __init__(self, first_vfd, last_vfd, conveyor_type, line):
        conveyor_types_dict = {"Distribution": ["D", "Dist"], "Transfer": ["T", "Trans"], "Accumulation": ["A", "Accum"], "Weigher Feeder": ["WF", "WF"], "Modulation": ["XF", "Mod"]}
        self.first_vfd = first_vfd
        self.last_vfd = last_vfd
        self.conveyor_type = conveyor_type
        self.conveyor_type_letter = conveyor_types_dict[conveyor_type][0]
        self.conveyor_type_short = conveyor_types_dict[conveyor_type][1]
    
        self.line = line
        self.frequencies_list = ["Max", "Min"]
        self.setpoint_timers = {"RunTmrOn": "RunTmrOnPre", "FwdWdg": "ForwardWdgPre"}


    def drives(self):
        dict_data = []
        dict1 = features()
        dict1[":IndirectAnalog"] = "Generic{}{}CSW".format(self.conveyor_type_short, self.line)            
        dict_data.append(dict1)

        return(dict_data) 


    def frequencies(self):
        dict_data = self.drives()
        for freq in self.frequencies_list:
            if self.conveyor_type == "Distribution" or self.conveyor_type == "Weigher Feeder":
                dict1 = features()
                dict1[":IndirectAnalog"] = "GenericEngWmDs{}{}{}Freq".format(self.conveyor_type_short, self.line, freq)
                dict_data.append(dict1)
            else:
                for i in range(self.first_vfd, self.last_vfd + 1):
                    dict1 = features()
                    dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}{}Freq".format(self.conveyor_type_short, i, freq)
                    dict_data.append(dict1)

        return(dict_data)        


    def speed_ref(self):
        dict_data = self.frequencies()
        accum_speeds_list = ["Ts", "Ds"]
        mod_speeds_list = ["Hi", "Lo"]

        if self.conveyor_type == "Distribution" or self.conveyor_type == "Weigher Feeder":
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericEngWmDs{}{}".format(self.conveyor_type_short, self.line)            
            dict_data.append(dict1)
        else:
            for i in range(self.first_vfd, self.last_vfd + 1):    
                if self.conveyor_type == "Accumulation":
                    for speed in accum_speeds_list:
                        dict1 = features()
                        dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}{}".format(self.conveyor_type_short, i, speed)
                        dict_data.append(dict1)

                elif self.conveyor_type == "Modulation":
                    for speed in mod_speeds_list:
                        dict1 = features()
                        dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}{}".format(self.conveyor_type_short, i, speed)
                        dict_data.append(dict1)
                    
                elif self.conveyor_type == "Transfer":
                    dict1 = features()
                    dict1[":IndirectAnalog"] = "GenericEngInfDs{}{}".format(self.conveyor_type_short, i) 
                    dict_data.append(dict1)

        return(dict_data) 


    def timers(self):
        dict_data = self.speed_ref()
        for timer in self.setpoint_timers.keys():
            if self.conveyor_type == "Distribution" or self.conveyor_type == "Weigher Feeder":
                dict1 = features()
                dict1[":IndirectAnalog"] = "GenericEngWmSp{}{}{}".format(self.conveyor_type_short, self.line, timer)            
                dict_data.append(dict1)
            else:
                for i in range(self.first_vfd, self.last_vfd + 1):    
                    dict1 = features()
                    dict1[":IndirectAnalog"] = "GenericEngInfSp{}{}{}".format(self.conveyor_type_short, i, timer)
                    dict_data.append(dict1)

        return(dict_data)


    def create_csv(self):
        csv_file = "csv-files/indirect/eng_{}_drives.csv".format(self.conveyor_type_short)
        dict_data = self.timers()
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
    wm = DrivesIndirectAnalog(1, 4, "Distribution", 'A')
    wm.create_csv()                 