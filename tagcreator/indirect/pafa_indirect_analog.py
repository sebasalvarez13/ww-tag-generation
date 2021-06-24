#!/usr/bin/env python3

import csv

class PAFAIndirectAnalog:
    def __init__(self):
        self.number_type = ["Decimal", "Percent"]
        self.outer_list = ["CV", "L", "PV"]
        

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


    def bag_speed(self):
        dict_data = []
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericPAFABagSpeed"
        dict_data.append(dict1)

        return(dict_data)


    def bag_weight(self):
        dict_data = self.bag_speed()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericPAFABagWeight"
        dict_data.append(dict1)

        return(dict_data) 


    def multiplier(self):
        dict_data = self.bag_weight()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericPAFAMultiplier"
        dict_data.append(dict1)

        return(dict_data) 


    def pid(self):
        dict_data = self.multiplier()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericPAFAPidSp"
        dict_data.append(dict1)

        return(dict_data) 


    def wf_trend(self):
        dict_data = self.pid()
        dict1 = self.features()
        dict1[":IndirectAnalog"] = "GenericPAFAWFTrend"
        dict_data.append(dict1)

        return(dict_data) 


    def bpm(self):
        dict_data = self.wf_trend()
        for number in self.number_type:
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericPAFABpmActual{}".format(number)
            dict_data.append(dict1)

        return(dict_data) 
 

    def duty_cycle(self):
        dict_data = self.bpm()
        for number in self.number_type:
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericPAFADutyCycle{}".format(number)
            dict_data.append(dict1)

        return(dict_data) 


    def outer(self):
        dict_data = self.duty_cycle()
        for outer in self.outer_list:
            dict1 = self.features()
            dict1[":IndirectAnalog"] = "GenericPAFAOuter{}".format(outer)
            dict_data.append(dict1)

        return(dict_data) 


    def create_csv(self):
        csv_file = "csv-files/indirect/pafa_indirect_analog.csv"
        dict_data = self.outer()
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
    wm = PAFAIndirectAnalog()
    wm.create_csv()
