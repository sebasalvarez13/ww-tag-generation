#!/usr/bin/env python3


from flask import Flask, render_template, request, redirect
#import pymysql
#from pymysql import connections
import os
import subprocess
import sys
import sqlite3
import glob
import pandas as pd
from combine_csv import MergedDataFrame
from module_signals import WeigherModule
from ltdiscrete import LTDiscrete
from lsdiscrete import LSDiscrete
from vfd_discrete import VFDDiscrete
from tags_display import tagdisplay

#from LTPackage.level_transmitter_integer import LevelTransmitterInteger
#from LTPackage.level_transmitter_real import LevelTransmitterReal

#import sqlalchemy
#import boto3
#from config import *

app = Flask(__name__)
output = {}
#table = 'revgate_faults'

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/LTTags", methods=['GET', 'POST'])
def AddLevelTransTags():
    first_transmitter = request.form["first_transmitter"]
    last_transmitter = request.form["last_transmitter"]
    transmitter_number = request.form["transmitter_number"]
    conveyor_type = request.form["conveyor_type"]
    line = request.form["line"]

    ltd = LTDiscrete(int(first_transmitter), int(last_transmitter), int(transmitter_number), conveyor_type, line)
    ltd.create_csv()

    return render_template('index.html')

@app.route("/LSTags", methods=['GET', 'POST'])
def AddLevelSensorTags():
    first_sensor = request.form["first_sensor"]
    last_sensor = request.form["last_sensor"]
    sensor_number = request.form["sensor_number"]
    conveyor_type = request.form["conveyor_type"]
    line = request.form["line"]

    lsd = LSDiscrete(int(first_sensor), int(last_sensor), int(sensor_number), conveyor_type, line)
    lsd.create_csv()

    return render_template('index.html')

@app.route("/WMTags", methods=['GET', 'POST'])
def AddModuleTags():
    first_module = request.form["first_module"]
    last_module = request.form["last_module"]

    wm = WeigherModule(int(first_module), int(last_module))
    wm.create_csv()

    return render_template('index.html')

@app.route("/VFDDiscreteTags", methods=['GET', 'POST'])
def AddVFDDiscreteTags():
    first_vfd = request.form["first_vfd"]
    last_vfd = request.form["last_vfd"]
    conveyor_type = request.form["conveyor_type"]
    line = request.form["line"]

    vfd = VFDDiscrete(int(first_vfd), int(last_vfd), conveyor_type, line)
    vfd.create_csv()

    return render_template('index.html')

@app.route("/AppendTags", methods = ["GET", "POST"])
def AppendTags():
    df_merged = MergedDataFrame.merge()
    df_merged.to_csv( "csv-files/merged.csv")
    
    return render_template("output.html")

@app.route("/DisplayTags", methods = ["GET", "POST"])
def DisplayTags():
    tagdisplay()
    return render_template("tagstable.html")    

@app.route("/about", methods=["GET", "POST"])
def about():
    return redirect("https://www.processsolutions.com/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
