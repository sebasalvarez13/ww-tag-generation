#!/usr/bin/env python3

import csv
from indirect_analog_features import features

class PAFAIndirectAnalog:
    def __init__(self):
        self.number_type = ["Decimal", "Percent"]
        self.outer_list = ["CV", "L", "PV"]
        self.bag_inputs = ["Speed", "Weight"]
        self.tag_start = "GenericPAFA"
        self.other_pafa_factors = ["Multiplier", "PidSp", "WFTrend"]


    def bag(self):
        dict_data = []
        for bag in self.bag_inputs:
            dict1 = features()
            dict1[":IndirectAnalog"] = "{}Bag{}".format(self.tag_start, bag)
            dict_data.append(dict1)

        return(dict_data)


    def other_factors(self):
        dict_data = self.bag()
        for factor in self.other_pafa_factors:
            dict1 = features()
            dict1[":IndirectAnalog"] = "{}{}".format(self.tag_start, factor)
            dict_data.append(dict1)

        return(dict_data) 


    def bpm(self):
        dict_data = self.other_factors()
        for number in self.number_type:
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericPAFABpmActual{}".format(number)
            dict_data.append(dict1)

        return(dict_data) 
 

    def duty_cycle(self):
        dict_data = self.bpm()
        for number in self.number_type:
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericPAFADutyCycle{}".format(number)
            dict_data.append(dict1)

        return(dict_data) 


    def outer(self):
        dict_data = self.duty_cycle()
        for outer in self.outer_list:
            dict1 = features()
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
