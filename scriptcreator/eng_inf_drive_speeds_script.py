#!/usr/bin/env python3

import csv
import textwrap
import glob

#from website_example import first_transmitter, last_transmitter, gate_num, line

class EngInfDriveSpeeds:
    def __init__(self, first_vfd, last_vfd, conveyor_type, line):
        conveyor_types_dict = {"Distribution": ["D", "Dist"], "Transfer": ["T", "Trans"], "Accumulation": ["A", "Accum"], "Weigher Feeder": ["WF", "WF"], "Modulation": ["XF", "Mod"]}
        line_numbers = {"A": 1, "B": 2, "C": 3, "D": 4}
        self.first_vfd = first_vfd
        self.last_vfd = last_vfd
        self.conveyor_type = conveyor_type

        self.conveyor_type_letter = conveyor_types_dict[conveyor_type][0]
        self.conveyor_type_short = conveyor_types_dict[conveyor_type][1]

        self.line = line
        

    def drive_speeds(self):
        accum_speeds = {"Transfer": "Ts", "Discharge": "Ds"}
        mod_speeds = ["Hi", "Lo"]
        line1 = ""
        line2 = ""
        
        if self.conveyor_type == "Accumulation":
            for i in range(self.first_vfd, self.last_vfd + 1):
                for j in accum_speeds.keys():
                    line1 = "GenericEngInfDs{}{}{}.Name = ".format(self.conveyor_type_short, i, accum_speeds[j])
                    line2 = "M{}{}{}_{}Mode_SpeedRef_SP.Name;".format(self.conveyor_type_letter, i, self.line, j)

                    str1 = (line1 + line2)
                    self.create_script(str1)
   
        elif self.conveyor_type == "Modulation":
            for i in range(self.first_vfd, self.last_vfd + 1):
                for j in mod_speeds:
                    line1 = "GenericEngInfDs{}{}{}.Name = ".format(self.conveyor_type_short, i, j)
                    line2 = "M{}{}{}_{}_SpeedRef_SP.Name;".format(self.conveyor_type_letter, i, self.line, j)

                    str1 = (line1 + line2)
                    self.create_script(str1)
             
        elif self.conveyor_type == "Transfer":
            for i in range(self.first_vfd, self.last_vfd + 1):
                line1 = "GenericEngInfDs{}{}.Name = ".format(self.conveyor_type_short, i)
                line2 = "M{}{}{}_SpeedRef_SP.Name;".format(self.conveyor_type_letter, i, self.line)

                str1 = (line1 + line2)
                self.create_script(str1)
        

    def create_script(self, str1):
        script_file = "window-scripts/script_infeed_drive_speeds.txt"
        try:
            with open(script_file, 'a') as scriptfile:
                scriptfile.write(textwrap.dedent(str1))
                scriptfile.write(textwrap.dedent("\n"))      
        except IOError as e:
            print(e)
        

if __name__ == "__main__":
    first_vfd = 1
    last_vfd = 3
    wm = WMScript(first_vfd, last_vfd, "Transfer", "A")
    """
    for i in range(first_module, (last_module + 1)):
        module = i
        str1 = wm.distribution(module)
        str2 = wm.weigher_feeder(module)
        str3 = wm.weigher(module)
        str4 = wm.pafa(module)
        str5 = wm.misc(module)
        wm.create_script(module, str1, str2, str3, str4, str5)
    """
    wm.speed_ref()
