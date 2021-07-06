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

        #This for loop goes through the files of the path directory passed as a parameter
        #if the file is not named "merged.csv", it will be appended to the filenames list 
        for f in glob.glob(path):
            if f != "/mnt/c/Projects/ww-tag-generation/csv-files/{folder}/merged.csv".format(folder = folder):
                filenames.append(f)

        #After filtering out the "merged.csv" file and having append all other files to filenames list
        #we loop through the filenames list and convert the.csv file to a dataframe
        #Finally, the generated dataframe is appended to a df_list 
        for f in filenames:
            df_from_each_file = (pd.read_csv(f, sep=','))
            df_list.append((df_from_each_file))

        #Concatenates all dataframe objects in df_list into a single dataframe called "df_merged"
        df_merged = pd.concat(df_list, ignore_index=False)


        return(df_merged)


    def mergeIO():
        #os.chdir("/mnt/c/Projects/ww-tag-generation/csv-files")
        file_extension = ".csv"
        filenames = []
        df_from_each_file = ()

        #This for loop iterates through all the .csv files in the "merged" directory
        #These are the final files contaning all tags respectively for discrete, integer, real, etc
        # The .csv files are appended to the filenames list 
        for f in glob.glob("/mnt/c/Projects/ww-tag-generation/csv-files/merged/*.csv"):
            filenames.append(f)

        #A dataframe list called "df-list" is declared
        df_list = []
        
        #We loop through the filenames list and convert the.csv file to a dataframe
        #Set header = none in order to read a csv in that doesn't have a header
        #Finally, the generated dataframe is appended to a df_list
        for f in filenames:
            df_from_each_file = (pd.read_csv(f, sep=',', header = None))
            df_list.append((df_from_each_file))

        #Declare a dataframe object called "df_appended"    
        df_appended = pd.DataFrame()

        #Iterates through the dataframes in df_list and appends them to datframe object "df_appended"
        # This generates a single dataframe object that contains all the types of tags  
        for frame in df_list:
            df_appended = df_appended.append(frame)


        return(df_appended)

if __name__ == "__main__":
    print(MergedDataFrame.mergeIO())