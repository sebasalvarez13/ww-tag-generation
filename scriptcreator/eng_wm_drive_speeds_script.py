#!/usr/bin/env python3

import csv
import textwrap
import os.path
from os import path


class EngWMDriveSpeeds:
    def __init__(self, first_vfd, last_vfd, conveyor_type, line):
        conveyor_types_dict = {"Distribution": ["D", "Dist"], "Transfer": ["T", "Trans"], "Accumulation": ["A", "Accum"], "Weigher Feeder": ["WF", "WF"], "Modulation": ["XF", "Mod"]}

        self.first_vfd = first_vfd
        self.last_vfd = last_vfd

        self.conveyor_type = conveyor_type
        self.conveyor_type_letter = conveyor_types_dict[conveyor_type][0]
        self.conveyor_type_short = conveyor_types_dict[conveyor_type][1]

        self.line = line

        self.accum_speeds = {"Transfer": "Ts", "Discharge": "Ds"}
        self.mod_speeds = {"Hi": "Max", "Lo": "Min"}
        self.frequencies_list = ["Max", "Min"]


    def header(self):
        line1 = """Module_Name = "Weigher Module "+Text(mem_wm+weigherOffset, "0"); """
        line2 = """ScreenTitle =  "Module Drive Speeds";"""
        line3 = """DIM windowStateInt AS INTEGER;"""
        line4 = """windowStateInt = WindowState("ENG - WM Menu");"""
        line5 = """IF windowStateInt == 0 THEN"""
        line6 = """Show("Eng - INF Menu");"""
        line7 = """ENDIF;""" 

        paragraph = [line1, line2, line3, line4, line5, line6, line7]

        for line in paragraph:
            self.print_to_script(line)


    def drive_speeds(self):
        line1 = "GenericEngWmDs{}{}.Name = ".format(self.conveyor_type_short, self.line)
        line2 = """ "M{}"+Text(mem_wm,"0")+"{}_SpeedRef_SP;" """.format(self.conveyor_type_letter, self.line)

        str1 = (line1 + line2)
        self.print_to_script(str1)


    def frequencies(self):
        line1 = ""
        line2 = ""
        
        for freq in self.frequencies_list:
            line1 = "GenericEngWmDs{}{}{}Freq.Name = ".format(self.conveyor_type_short, self.line, freq)
            line2 = """ "M{}"+Text(mem_wm,"0")+"{}_{}_Frequency;" """.format(self.conveyor_type_letter, self.line, freq)

            str1 = (line1 + line2)
            self.print_to_script(str1)


    def print_to_script(self, str1):
        script_file = "window-scripts/script_wm_drive_speeds.txt"
        try:
            with open(script_file, 'a') as scriptfile:
                scriptfile.write(textwrap.dedent(str1))
                scriptfile.write(textwrap.dedent("\n"))      
        except IOError as e:
            print(e)


    def script_exists(self):
        file_path = "/mnt/c/Projects/ww-tag-generation/window-scripts/script_wm_drive_speeds.txt"
        if path.exists(file_path):
            return True
        else:
            return False  


    def create_script(self):
        if self.script_exists() != True :
            self.header()
            self.print_to_script(" ")

        self.drive_speeds()
        self.frequencies()
        self.print_to_script(" ")                   
               

if __name__ == "__main__":
    first_vfd = 1
    last_vfd = 5
    wm = EngWMDriveSpeeds(first_vfd, last_vfd, "Weigher Feeder", "")
    wm.create_script()
    
