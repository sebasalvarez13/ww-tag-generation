#!/usr/bin/env python3

import csv
import textwrap

#from website_example import first_transmitter, last_transmitter, gate_num, line

class WMScript:
    def __init__(self, first_module, last_module, transmitter_number, conveyor_type, line):
        conveyor_types = {"Distribution": "D", "Transfer": "T", "Accumulation": "A", "Weigher Feeder": "WF", "Modulation": "X"}
        line_numbers = {"A": 1, "B": 2, "C": 3, "D": 4}
        self.first_module = first_module
        self.last_module = last_module
        self.transmitter_number = transmitter_number
        self.conveyor_type = conveyor_type
        self.conveyor_type_letter = conveyor_types[conveyor_type]
        self.line = line
        self.line_number = line_numbers[line]

    def distribution(self, module):
        line1 = """GenericDistACSW.Name = "M{conveyor_type_letter}{module}{line}_CSW";""".format(conveyor_type_letter = self.conveyor_type_letter, module = module, line = self.line)
        line2 = """GenericRevGateAProductAvailable.Name = "WM{module}_RVG{line_number}M_Product_Available";""".format(module = module, line_number = self.line_number)
        line3 = """GenericRevGateALevelTrans.Name = "LT{transmitter_number}{conveyor_type_letter}{module}{line}_Fltrd";""".format(transmitter_number = self.transmitter_number, conveyor_type_letter = self.conveyor_type_letter, module = module, line = self.line)
        line4 = """GenericPkgWmGateACSW.Name = "PkgAutoSys_WeighMod{module}_Gate{line}_CSW";""".format(module = module, line = self.line)
        line5 = """GenericRevGateAStatus.Name = "WM{module}_RVG{line_number}M_O_Status";""".format(module = module, line_number = self.line_number)
        line6 = """GenericRevGateAAngleSts.Name = "WM{module}_RVG{line_number}M_O_AngleSts";""".format(module = module, line_number = self.line_number)

        paragraph = [line1, line2, line3, line4, line5, line6]

        last_line = ""
        for line in paragraph:
            last_line = last_line + line + "\n"

        return(last_line)
        

    def weigher_feeder(self, module):
        line1 = """GenericWFCSW.Name = "MWF{module}_CSW";""".format(module = module)

        return(line1)


    def weigher(self, module):
        line1 = """
        GenericCallForProduct.Name = "WM{module}_Call_For_Product";
        GenericInfeedEnable.Name = "WM{module}_Infeed_Enable";""".format(module = module)

        return(line1)    
    

    def pafa(self, module):
        line1 = """
        GenericPAFAGreenEff.Name = "WM{module}_PAFA_Green";
        GenericPAFAYellowEff.Name = "WM{module}_PAFA_Yellow";
        GenericPAFARedEff.Name = "WM{module}_PAFA_Red";
        GenericPAFABagSpeed.Name = "WM{module}_Control_OIT_BagSpeed";
        GenericPAFABagWeight.Name = "WM{module}_Control_OIT_BagWeight";
        GenericPAFABpmActual.Name = "WM{module}_ModuleStats_BPM";
        GenericPAFADutyCyclePercent.Name = "WM{module}_ModuleStats_DC_Percent";
        GenericPAFAOuterPV.Name = "WM{module}_PAFA_PV";
        GenericPAFAMultiplier.Name = "WM{module}_Module_M";
        GenericPAFASuspension.Name = "WM{module}_PAFA_Permissive";
        GenericPAFAPidSp.Name = PAFA_Global_Setpoint.Name;""".format(module = module)

        return(line1)


    def misc(self, module):
        line1 = """
        GenericPkgWmCSW.Name = "PkgAutoSys_WeighMod{module}_CSW";""".format(module = module)

        return(line1)


    def create_script(self, module, str1, str2, str3, str4, str5):
        script_file = "window-scripts/script{}.txt".format(module)
        try:
            with open(script_file, 'w') as scriptfile:
                scriptfile.write(textwrap.dedent(str1))
                scriptfile.write(textwrap.dedent("\n"))     
                scriptfile.write(textwrap.dedent(str2)) 
                scriptfile.write(textwrap.dedent("\n"))     
                scriptfile.write(textwrap.dedent(str3))     
                scriptfile.write(textwrap.dedent("\n"))     
                scriptfile.write(textwrap.dedent(str4))
                scriptfile.write(textwrap.dedent("\n"))     
                scriptfile.write(textwrap.dedent(str5))      
        except IOError as e:
            print(e)


if __name__ == "__main__":
    first_module = 1
    last_module = 3
    wm = WMScript(first_module, last_module, 1, "Distribution", "A")
    for i in range(first_module, (last_module + 1)):
        module = i
        str1 = wm.distribution(module)
        str2 = wm.weigher_feeder(module)
        str3 = wm.weigher(module)
        str4 = wm.pafa(module)
        str5 = wm.misc(module)
        wm.create_script(module, str1, str2, str3, str4, str5)
    
