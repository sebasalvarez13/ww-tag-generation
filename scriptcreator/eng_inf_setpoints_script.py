#!/usr/bin/env python3

import csv
import textwrap
import os.path
from os import path


class EngInfSetpoints:
    def __init__(self, first_vfd, last_vfd, conveyor_type, line):
        conveyor_types_dict = {"Distribution": ["D", "Dist"], "Transfer": ["T", "Trans"], "Accumulation": ["A", "Accum"], "Weigher Feeder": ["WF", "WF"], "Modulation": ["XF", "Mod"]}

        self.first_vfd = first_vfd
        self.last_vfd = last_vfd

        self.conveyor_type = conveyor_type
        self.conveyor_type_letter = conveyor_types_dict[conveyor_type][0]
        self.conveyor_type_short = conveyor_types_dict[conveyor_type][1]

        self.line = line

        self.setpoint_timers = {"RunTmrOn": "RunTmrOnPre", "FwdWdg": "ForwardWdgPre"}

        self.mod_speeds = {"Hi": "Max", "Lo": "Min"}
        self.frequencies_list = ["Max", "Min"]


    def header(self):
        line1 = """Module_Name = "";"""
        line2 = """ScreenTitle =  "Infeed Setpoints";"""
        line3 = """DIM windowStateInt AS INTEGER;"""
        line4 = """windowStateInt = WindowState("ENG - INF Menu");"""
        line5 = """IF windowStateInt == 0 THEN"""
        line6 = """Show("Eng - INF Menu");"""
        line7 = """ENDIF;""" 

        paragraph = [line1, line2, line3, line4, line5, line6, line7]

        for line in paragraph:
            self.print_to_script(line)


    def setpoints(self):
        line1 = ""
        line2 = ""
        
        for i in range(self.first_vfd, self.last_vfd + 1):
            for j in self.setpoint_timers.keys():
                line1 = "GenericEngInfSp{}{}{}.Name = ".format(self.conveyor_type_short, i, j)
                line2 = "M{}{}{}_{}.Name;".format(self.conveyor_type_letter, i, self.line, self.setpoint_timers[j])

                str1 = (line1 + line2)
                self.print_to_script(str1)


    def text(self):
        line1 = ""
        line2 = ""

        for i in range(self.first_vfd, self.last_vfd + 1):   
            line1 = "GenericEngInfSp{}{}Text = ".format(self.conveyor_type_short, i)
            line2 = """ "{} Conveyor M{}{}{} Timer" """.format(self.conveyor_type, self.conveyor_type_letter, i, self.line)

            str1 = (line1 + line2)
            self.print_to_script(str1)


    def print_to_script(self, str1):
        script_file = "window-scripts/script_infeed_setpoints.txt"
        try:
            with open(script_file, 'a') as scriptfile:
                scriptfile.write(textwrap.dedent(str1))
                scriptfile.write(textwrap.dedent("\n"))      
        except IOError as e:
            print(e)


    def script_exists(self):
        file_path = "/mnt/c/Projects/ww-tag-generation/window-scripts/script_infeed_setpoints.txt"
        if path.exists(file_path):
            return True
        else:
            return False  


    def create_script(self):
        if self.script_exists() != True :
            self.header()
            self.print_to_script(" ")

        self.setpoints()
        self.text()
        self.print_to_script(" ")                   
               

if __name__ == "__main__":
    first_vfd = 1
    last_vfd = 3
    wm = EngInfSetpoints(first_vfd, last_vfd, "Transfer", "A")
    wm.create_script()
    
