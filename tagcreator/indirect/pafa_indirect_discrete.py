#!/usr/bin/env python3

import csv

class PAFAIndirectDiscrete:
    def __init__(self):
        self.lines = ["A", "B", "C", "D"]
        

    def features(self):
        dict_data = []
        my_dict = {
            ":IndirectDisc":"",
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


    def suspension(self):
        dict_data = []
        dict1 = self.features()
        dict1[":IndirectDisc"] = "GenericPAFASuspension"
        dict_data.append(dict1)

        return(dict_data) 


    def green_efficiency(self):
        dict_data = self.suspension()
        dict1 = self.features()
        dict1[":IndirectDisc"] = "GenericPAFAGreenEff"
        dict_data.append(dict1)

        return(dict_data)


    def yellow_efficiency(self):
        dict_data = self.green_efficiency()
        dict1 = self.features()
        dict1[":IndirectDisc"] = "GenericPAFAYellowEff"
        dict_data.append(dict1)

        return(dict_data)


    def red_efficiency(self):
        dict_data = self.yellow_efficiency()
        dict1 = self.features()
        dict1[":IndirectDisc"] = "GenericPAFARedEff"
        dict_data.append(dict1)

        return(dict_data)     


    def create_csv(self):
        csv_file = "csv-files/discrete/pafa_indirect.csv"
        dict_data = self.red_efficiency()
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
    wm = PAFAIndirectDiscrete()
    wm.create_csv()
