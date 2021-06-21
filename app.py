#!/usr/bin/env python3


from flask import Flask, render_template, request, redirect

import os
import subprocess
import sys
import sqlite3
import glob
import pandas as pd

from tagcreator.discrete.wm_discrete import WMDiscrete
from tagcreator.discrete.lt_discrete import LTDiscrete
from tagcreator.discrete.ls_discrete import LSDiscrete
from tagcreator.discrete.vfd_discrete import VFDDiscrete
from tagcreator.discrete.sg_discrete import SGDiscrete
from tagcreator.discrete.pafa_discrete import PAFADiscrete

from tagcreator.integer.lt_integer import LTInteger
from tagcreator.integer.vfd_integer import VFDInteger
from tagcreator.integer.wm_integer import WMInteger
from tagcreator.integer.rvg_integer import RVGInteger
from tagcreator.integer.pkgautosys_integer import PkgAutoSysInteger
from tagcreator.integer.afa_integer import AFAInteger

from tagcreator.real.lt_real import LTReal
from tagcreator.real.pafa_real import PAFAReal
from tagcreator.real.rvg_real import RVGReal
from tagcreator.real.wm_real import WMReal
from tagcreator.real.wmstats_real import WMStatsReal

from tagcreator.indirect.inf_drives_indirect_analog import InfDrivesIndirectAnalog

from tags_display import tagdisplay
from scriptcreator.wm_script import WMScript
from scriptcreator.eng_inf_drive_speeds_script import EngInfDriveSpeeds
from combine_csv import MergedDataFrame


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/lt", methods=['GET', 'POST'])
def AddLevelTransTags():
    first_transmitter = request.form["first_transmitter"]
    last_transmitter = request.form["last_transmitter"]
    transmitter_number = request.form["transmitter_number"]
    conveyor_type = request.form["conveyor_type"]
    line = request.form["line"]

    ltd = LTDiscrete(int(first_transmitter), int(last_transmitter), int(transmitter_number), conveyor_type, line)
    ltd.create_csv()

    lti = LTInteger(int(first_transmitter), int(last_transmitter), int(transmitter_number), conveyor_type, line)
    lti.create_csv()

    ltr = LTReal(int(first_transmitter), int(last_transmitter), int(transmitter_number), conveyor_type, line)
    ltr.create_csv()

    return render_template('index.html')


@app.route("/ls", methods=['GET', 'POST'])
def AddLevelSensorTags():
    first_sensor = request.form["first_sensor"]
    last_sensor = request.form["last_sensor"]
    sensor_number = request.form["sensor_number"]
    conveyor_type = request.form["conveyor_type"]
    line = request.form["line"]

    lsd = LSDiscrete(int(first_sensor), int(last_sensor), int(sensor_number), conveyor_type, line)
    lsd.create_csv()

    return render_template('index.html')


@app.route("/wm", methods=['GET', 'POST'])
def AddModuleTags():
    first_module = request.form["first_module"]
    last_module = request.form["last_module"]

    wm = WMDiscrete(int(first_module), int(last_module))
    wm.create_csv()

    wmi = WMInteger(int(first_module), int(last_module))
    wmi.create_csv()

    wmr = WMReal(int(first_module), int(last_module))
    wmr.create_csv()

    wmstats = WMStatsReal(int(first_module), int(last_module))
    wmstats.create_csv()

    return render_template('index.html')


@app.route("/vfd", methods=['GET', 'POST'])
def AddVFDDiscreteTags():
    first_vfd = request.form["first_vfd"]
    last_vfd = request.form["last_vfd"]
    conveyor_type = request.form["conveyor_type"]
    line = request.form["line"]

    vfd = VFDDiscrete(int(first_vfd), int(last_vfd), conveyor_type, line)
    vfd.create_csv()

    vfdi = VFDInteger(int(first_vfd), int(last_vfd), conveyor_type, line)
    vfdi.create_csv()

    vfd_ind_analog = InfDrivesIndirectAnalog(int(first_vfd), int(last_vfd), conveyor_type, line)
    vfd_ind_analog.create_csv()

    inf_drive_speeds = EngInfDriveSpeeds(int(first_vfd), int(last_vfd), conveyor_type, line)
    inf_drive_speeds.drive_speeds()

    return render_template('index.html')


@app.route("/sg", methods=['GET', 'POST'])
def AddSlideGateTags():
    first_gate = request.form["first_gate"]
    last_gate = request.form["last_gate"]
    gate_number = request.form["gate_number"]
    conveyor_type = request.form["conveyor_type"]
    line = request.form["line"]

    sg = SGDiscrete(int(first_gate), int(last_gate), int(gate_number), conveyor_type, line)
    sg.create_csv()

    return render_template('index.html')


@app.route("/pafa", methods=['GET', 'POST'])
def AddPAFATags():
    first_module = request.form["first_module"]
    last_module = request.form["last_module"]

    pafad = PAFADiscrete(int(first_module), int(last_module))
    pafad.create_csv()

    pafar = PAFAReal(int(first_module), int(last_module))
    pafar.create_csv()

    return render_template('index.html')


@app.route("/pkgautosys", methods=['GET', 'POST'])
def Addpkgautosys():
    first_module = request.form["first_module"]
    last_module = request.form["last_module"]
    line = request.form["line"]

    pkg = PkgAutoSysInteger(int(first_module), int(last_module), line)
    pkg.create_csv()

    return render_template('index.html')


@app.route("/revgates", methods=['GET', 'POST'])
def Addrevgates():
    first_gate = request.form["first_gate"]
    last_gate = request.form["last_gate"]
    line = request.form["line"]

    rvgi = RVGInteger(int(first_gate), int(last_gate), line)
    rvgi.create_csv()

    rvgr = RVGReal(int(first_gate), int(last_gate), line)
    rvgr.create_csv()

    return render_template('index.html')


@app.route("/afa", methods=['GET', 'POST'])
def Addafa():
    line = request.form["line"]

    afai = AFAInteger(line)
    afai.create_csv()

    return render_template('index.html')


@app.route("/wmscripts", methods=['GET', 'POST'])
def AddWMWindowScripts():
    first_module = request.form["first_module"]
    last_module = request.form["last_module"]
    transmitter_number = request.form["transmitter_number"]
    conveyor_type = request.form["conveyor_type"]
    line = request.form["line"]

    wm = WMScript(int(first_module), int(last_module), int(transmitter_number), conveyor_type, line)
    for i in range(int(first_module), (int(last_module) + 1)):
        module = i
        str1 = wm.distribution(module)
        str2 = wm.weigher_feeder(module)
        str3 = wm.weigher(module)
        str4 = wm.pafa(module)
        str5 = wm.misc(module)
        wm.create_script(module, str1, str2, str3, str4, str5)

    return render_template('index.html')


@app.route("/appendtags", methods = ["GET", "POST"])
def AppendTags():
    folders = ["discrete", "integer", "indirect", "real"]
    #creates a csv file for each type of tag: integer, discrete, real, etc
    for f in folders:
        path = "csv-files/merged/{}_merged.csv".format(f)
        df_merged = MergedDataFrame.merge(f)
        df_merged.to_csv(path, index = False, encoding = "utf-8-sig")

    #combines the integer, discrete, real, etc csv files into one final csv ready to DBload
    df_combined = MergedDataFrame.mergeIO()
    df_combined.to_csv("csv-files/merged/final.csv", index = False, encoding = "utf-8-sig")

    return render_template("output.html")


@app.route("/displaytags", methods = ["GET", "POST"])
def DisplayTags():
    tagdisplay()
    return render_template("tagstable.html")    


@app.route("/about", methods=["GET", "POST"])
def about():
    return redirect("https://www.processsolutions.com/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)