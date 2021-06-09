#!/usr/bin/env python3

import csv
#from website_example import first_transmitter, last_transmitter, gate_num, line

class VFDInteger:
    def __init__(self, first_vfd, last_vfd, conveyor_type, line):
        conveyor_types = {"Distribution": "D", "Transfer": "T", "Accumulation": "A", "Weigher Feeder": "WF", "Modulation": "XF"}
        self.first_vfd = first_vfd
        self.last_vfd = last_vfd
        self.conveyor_type = conveyor_type
        self.conveyor_type_letter = conveyor_types[conveyor_type]
        self.line = line

        if self.conveyor_type == "Weigher Feeder":
            self.line = ""
            

    def features(self):
        """Features for IO Integer Tags"""
        dict_data = []
        my_dict = {
            ":IOInt":"",
            "Group": "$System",
            "Comment": "",
            "Logged": "No",
            "EventLogged": "No",
            "EventLoggingPriority": 0,
            "RetentiveValue": "No",
            "RetentiveAlarmParameters": "No",
            "AlarmValueDeadband": 0,
            "AlarmDevDeadband": 0,
            "EngUnits": "",
            "InitialValue": 0,
            "MinEU": -32768,
            "MaxEU": 32767,
            "Deadband": 0,
            "LogDeadband": 0,
            "LoLoAlarmState": "Off",
            "LoLoAlarmValue": 0,
            "LoLoAlarmPri": 1,
            "LoAlarmState": "Off",
            "LoAlarmValue": 0,
            "LoAlarmPri": 1,
            "HiAlarmState": "Off",
            "HiAlarmValue": 0,
            "HiAlarmPri": 1,
            "HiHiAlarmState":  "Off",
            "HiHiAlarmValue": 0,
            "HiHiAlarmPri": 1,
            "MinorDevAlarmState": "Off",
            "MinorDevAlarmValue": 0,
            "MinorDevAlarmPri": 1,
            "MajorDevAlarmState": "Off",
            "MajorDevAlarmValue": 0,
            "MajorDevAlarmPri": 1,
            "DevTarget": 0,
            "ROCAlarmState": "Off",
            "ROCAlarmValue": 0,
            "ROCAlarmPri": 1,
            "ROCTimeBase": "Min",
            "MinRaw": -32768,
            "MaxRaw": 32767,
            "Conversion": "Linear",
            "AccessName": "HC",
            "ItemUseTagname": "No",
            "ItemName": "",
            "ReadOnly": "No",
            "AlarmComment": "",
            "AlarmAckModel": 0,
            "LoLoAlarmDisable": 0,
            "LoAlarmDisable": 0,
            "HiAlarmDisable": 0,
            "HiHiAlarmDisable": 0,
            "MinDevAlarmDisable": 0,
            "MajDevAlarmDisable": 0,
            "RocAlarmDisable": 0,
            "LoLoAlarmInhibitor": "",
            "LoAlarmInhibitor": "",
            "HiAlarmInhibitor": "",
            "HiHiAlarmInhibitor": "",
            "MinDevAlarmInhibitor": "",
            "MajDevAlarmInhibitor": "",
            "RocAlarmInhibitor": "",
            "SymbolicName": "",
        }

        dict_data.append(my_dict)

        return(my_dict)


    def csw(self):
        dict_data = []
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IOInt"] = "M{}{}{}_CSW".format(self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "M{}{}{}.CSW".format(self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)


    def runtimer(self):
        dict_data = self.csw()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IOInt"] = "M{}{}{}_RunTmrOnPre".format(self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "M{}{}{}.RunTmrOn.Pre".format(self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)        


    def forwardwdg(self):
        dict_data = self.runtimer()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IOInt"] = "M{}{}{}_ForwardWdgPre".format(self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "M{}{}{}.ForwardWdg.Pre".format(self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data)


    def speedref(self):
        dict_data = self.forwardwdg()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IOInt"] = "M{}{}{}_SpeedRef_SP".format(self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "M{}{}{}_SpeedRef_SP_Entry".format(self.conveyor_type_letter, i, self.line)

            dict_data.append(dict1)

        return(dict_data) 


    def max_freq(self):
        dict_data = self.speedref()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IOInt"] = "M{}{}{}_Max_Frequency".format(self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "M{}{}{}_VFD:I.MaximumFreq".format(self.conveyor_type_letter, i, self.line)
            dict1["MinEU"] = 0
            dict1["MaxEU"] = 1000
            dict1["MinRaw"] = 0
            dict1["MaxRaw"] = 100000
            dict_data.append(dict1)

        return(dict_data)
        
        
    def min_freq(self):
        dict_data = self.max_freq()
        for i in range(self.first_vfd, self.last_vfd + 1):
            dict1 = self.features()
            dict1[":IOInt"] = "M{}{}{}_Min_Frequency".format(self.conveyor_type_letter, i, self.line)
            dict1["ItemName"] = "M{}{}{}_VFD:I.MinimumFreq".format(self.conveyor_type_letter, i, self.line)
            dict1["MinEU"] = 0
            dict1["MaxEU"] = 1000
            dict1["MinRaw"] = 0
            dict1["MaxRaw"] = 100000
            dict_data.append(dict1)

        return(dict_data)          


    def create_csv(self):
        csv_file = "csv-files/integer/vfd_integer_{}_{}.csv".format(self.conveyor_type, self.line)
        dict_data = self.min_freq()
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
    wm = VFDInteger(10, 13, "Distribution", "C")
    wm.create_csv()            