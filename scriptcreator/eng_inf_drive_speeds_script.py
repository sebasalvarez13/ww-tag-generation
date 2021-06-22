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

    def header(self):
        line1 = """Module_Name = "";"""
        line2 = """ScreenTitle =  "Infeed Drive Speeds";"""
        line3 = """DIM windowStateInt AS INTEGER;"""
        line4 = """windowStateInt = WindowState("ENG - INF Menu");"""
        line5 = """IF windowStateInt == 0 THEN"""
        line6 = """Show("Eng - INF Menu");"""
        line7 = """ENDIF;""" 

        paragraph = [line1, line2, line3, line4, line5, line6, line7]

        for line in paragraph:
            self.create_script(line)


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


    def text(self):
        accum_speeds = {"Transfer": "Ts", "Discharge": "Ds"}
        mod_speeds = {"Hi": "Max", "Lo": "Min"}
        line1 = ""
        line2 = ""
   
        if self.conveyor_type == "Modulation":
            for i in range(self.first_vfd, self.last_vfd + 1):
                for j in mod_speeds.keys():
                    line1 = "GenericEngInfDs{}{}.Text = ".format(self.conveyor_type_short, i, j)
                    line2 = "{} Conveyor M{}{}{} {} Speed.Text;".format(self.conveyor_type, self.conveyor_type_letter, i, self.line, mod_speeds[j])

                    str1 = (line1 + line2)
                    self.create_script(str1)
             
        else:
            for i in range(self.first_vfd, self.last_vfd + 1):
                line1 = "GenericEngInfDs{}{}.Text = ".format(self.conveyor_type_short, i)
                line2 = "{} Conveyor M{}{}{}".format(self.conveyor_type, self.conveyor_type_letter, i, self.line)

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
    wm = EngInfDriveSpeeds(first_vfd, last_vfd, "Transfer", "A")
    wm.header()
    wm.drive_speeds()
