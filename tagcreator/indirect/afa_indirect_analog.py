#!/usr/bin/env python3

import csv
from tagcreator.indirect.indirect_analog_features import features


class AFAIndirectAnalog:
    def __init__(self):
        self.lines = ["A", "B", "C", "D"]
        self.afa_variables = ["CV", "KD", "KI", "KP", "PV", "SP"]
        self.derated_list = ["Coarse", "Fine", "Medium", "No"]
        

    def derated_percent(self):
        dict_data = []
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericAFADeratedPercent"
        dict_data.append(dict1)

        return(dict_data) 


    def afa_derating_percent(self):
        dict_data = self.derated_percent()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericEngAFADeratingPercent"
        dict_data.append(dict1)

        return(dict_data)


    def afa_last_active(self):
        dict_data = self.afa_derating_percent()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericAFALastActiveBPMPercent"
        dict_data.append(dict1)

        return(dict_data)


    def afa_multiplier(self):
        dict_data = self.afa_last_active()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericAFAMultiplier"
        dict_data.append(dict1)

        return(dict_data)


    def afa_pid(self):
        dict_data = self.afa_multiplier()
        for i in self.afa_variables:
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericAFAPID_{}".format(i)
            dict_data.append(dict1)

        return(dict_data)


    def afa_accum_full_suspend(self):         
        dict_data = self.afa_pid()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericEngAFAAccumFullSuspend"
        dict_data.append(dict1)

        return(dict_data)


    def adjust_amount(self):
        dict_data = self.afa_accum_full_suspend()
        for adjust in self.derated_list[0:3]:
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericEngAFA{}AdjAmt".format(adjust)

            dict_data.append(dict1)

        return(dict_data)    


    def neg_limit(self):
        dict_data = self.adjust_amount() 
        for adjust in self.derated_list:
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericEngAFA{}AdjNeg".format(adjust)

            dict_data.append(dict1)

        return(dict_data)


    def pos_limit(self):
        dict_data = self.neg_limit() 
        for adjust in self.derated_list:
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericEngAFA{}AdjPos".format(adjust)

            dict_data.append(dict1)

        return(dict_data)


    def d1_off_debounce(self):
        dict_data = self.pos_limit()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericEngAFAD1OffDebounce"

        dict_data.append(dict1)

        return(dict_data)      


    def d1_off_suspend(self):
        dict_data = self.d1_off_debounce()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericEngAFAD1OffSuspend"

        dict_data.append(dict1)

        return(dict_data) 


    def m_values(self):
        dict_data = self.d1_off_suspend()
        m_values_list = ["Max", "Min", "Reset"]
        for i in m_values_list:
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericEngAFA{}M".format(i)
            dict_data.append(dict1)

        return(dict_data) 


    def max_spd_debounce(self):
        dict_data = self.m_values()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericEngAFAMaxSpeedDebounce"
        dict_data.append(dict1)

        return(dict_data)


    def max_spd_suspend(self):
        dict_data = self.max_spd_debounce()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericEngAFAMaxSpeedSuspend"
        dict_data.append(dict1)

        return(dict_data)  


    def recirc_time(self):
        dict_data = self.max_spd_suspend()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericEngAFARecircTime"
        dict_data.append(dict1)

        return(dict_data)


    def sample_time(self):
        dict_data = self.recirc_time()
        dict1 = features()
        dict1[":IndirectAnalog"] = "GenericEngAFASampleTime"
        dict_data.append(dict1)

        return(dict_data)                 


    def purge(self):
        dict_data = self.sample_time()
        purge_values_list = ["Override", "Timer"]
        for i in purge_values_list:
            dict1 = features()
            dict1[":IndirectAnalog"] = "GenericEngAFAPurge{}".format(i)
            dict_data.append(dict1)

        return(dict_data) 


    def create_csv(self):
        csv_file = "csv-files/indirect/afa_indirect_analog.csv"
        dict_data = self.purge()
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
    wm = AFAIndirectAnalog()
    wm.create_csv()
