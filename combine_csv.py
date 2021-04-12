#!/usr/bin/env python3

import os
import glob
import pandas as pd


class MergedDataFrame():
    def __init__(self):
        pass

    def merge(folder):
        #os.chdir("/mnt/c/Projects/ww-tag-generation/csv-files")
        file_extension = ".csv"
        filenames = []
        df_list = []
        df_from_each_file = ()
        folder = folder
        path = "/mnt/c/Projects/ww-tag-generation/csv-files/{folder}/*.csv".format(folder = folder)

        for f in glob.glob(path):
            if f != "/mnt/c/Projects/ww-tag-generation/csv-files/{folder}/merged.csv".format(folder = folder):
                filenames.append(f)

        for f in filenames:
            df_from_each_file = (pd.read_csv(f, sep=','))
            df_list.append((df_from_each_file))

        #merges all files in list df_list
        df_merged = pd.concat(df_list, ignore_index=False)

        return(df_merged)


    def mergeIO():
        #os.chdir("/mnt/c/Projects/ww-tag-generation/csv-files")
        file_extension = ".csv"
        filenames = []
        df_from_each_file = ()

        for f in glob.glob("/mnt/c/Projects/ww-tag-generation/csv-files/merged/*.csv"):
            filenames.append(f)
            #if f != "/mnt/c/Projects/ww-tag-generation/csv-files/merged.csv":
             #   filenames.append(f)

        df_list = []
        
        for f in filenames:
            df_from_each_file = (pd.read_csv(f, sep=',', header = None))
            df_list.append((df_from_each_file))
            
        df_appended = pd.DataFrame()  
        for frame in df_list:
            df_appended = df_appended.append(frame)


        return(df_appended)

if __name__ == "__main__":
    print(MergedDataFrame.mergeIO())