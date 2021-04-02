import os
import glob
import pandas as pd


class MergedDataFrame():
    def __init__(self):
        pass

    def merge():
        #os.chdir("/mnt/c/Projects/ww-tag-generation/csv-files")
        file_extension = ".csv"
        filenames = []
        df_from_each_file = ()

        for f in glob.glob("/mnt/c/Projects/ww-tag-generation/csv-files/*.csv"):
            filenames.append(f)
        
        if f in filenames is "merged.csv":
            filenames.remove("merged.csv")
        #print(filenames)

        #print(type(df_from_each_file))
        #print(df_from_each_file)    


        #filenames = [i for i in glob.glob(f"*{file_extension}")]
        df_from_each_file = (pd.read_csv(f, sep=',') for f in filenames)
        df_merged = pd.concat(df_from_each_file, ignore_index=False)
        #print(df_merged)
        #print(df_merged.drop(df_merged.columns[3], axis = 1))

        return(df_merged)
#Combine all files in the list
#combined_csv = pd.concat([pd.read_csv(f, delimiter='t', encoding='UTF-16') for f in filenames])

#Export to csv
#combined_csv.to_csv( "alltags.csv", index = False, encoding = "utf-8-sig")
if __name__ == "__main__":
    MergedDataFrame.merge()