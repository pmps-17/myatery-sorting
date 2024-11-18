import pandas as pd
import math
import os
import csv
import numpy as np
import sys
sys.path.append("../Sorting_Algorithms")
from sorting_algos import merge_sort


column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']

####################################################################################
# Donot Modify this Code
####################################################################################
class FixedSizeList(list):
    def __init__(self, size):
        self.max_size = size

    def append(self, item):
        if len(self) >= self.max_size:
            raise Exception("Cannot add item. List is full.")
        else:
            super().append(item)
            

####################################################################################
# Mystery_Function
####################################################################################
def Mystery_Function(file_path, memory_limitation, columns):
    """
    # file_path :  file_path for Individual Folder (datatype : String)
    # memory_limitation : At each time how many records from the dataframe can be loaded (datatype : integer : 2000)
    # columns : the columns on which dataset needs to be sorted (datatype : list of strings)
    # Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
    # **NOTE : In this Mystery_Function records are accessed from only the folder Individual.

    #Store all the output files in Folder named "Final".
    #The below Syntax will help you to store the sorted files :
                # name_of_csv = "Final/Sorted_" + str(i + 1)
                # sorted_df.reset_index(drop=True).to_csv(name_of_csv, index=False)
    #Output csv files must be named in the format Sorted_1, Sorted_2,...., Sorted_93
    # ***NOTE : Every output csv file must have 2000 sorted records except for the last ouput csv file which might have less
                #than 2000 records.
    """
    cols=['tconst']
    column_vals = [0]
    for column in columns:
        if(column == 'tconst'):
            continue
        index = column_names.index(column)
        column_vals.append(index)
        cols.append(column)
        
    chuncks_2000=FixedSizeList(2000)
    id_files=[]
    for fileName in os.listdir(file_path):
        chuncks_2000=pd.read_csv(file_path+"/"+fileName).values.tolist()
        id_files.append(chuncks_2000)
    temp = []
    total_files = len(id_files)
    for i in range(len(id_files)):
        if(len(id_files[i])>1):
            data = id_files[i].pop(0)
            if data:
                temp.append((data, i))
    f_file=[]
    j=1
    while temp:
        if(len(f_file)<=memory_limitation):
            temp = f_merge_sort(temp , column_vals)
            f_data, f_i = temp.pop(0)
            f_file.append(f_data)
            if len(f_file)==memory_limitation and j<total_files:
                f_sorted=pd.DataFrame(f_file, columns=cols)
                name_of_csv = "Final/Sorted_" + str(j) + ".csv"
                f_sorted.reset_index(drop=True).to_csv(name_of_csv, index=False)
                f_file=[]
                j=j+1
            elif len(f_file)<=memory_limitation and j==total_files:
                f_sorted=pd.DataFrame(f_file, columns=cols)
                name_of_csv = "Final/Sorted_" + str(j) + ".csv"
                f_sorted.reset_index(drop=True).to_csv(name_of_csv, index=False)
            if len(id_files[f_i])>0:
                data = id_files[f_i].pop(0) 
                f_temp=[data, f_i]
                if data:
                   temp.append(f_temp)
        else:
            f_file=[]
        
                  
        

    #Need to Code
    #Helps to Sort all the 1,84,265 rows with limitation.

    #Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
    
    

####################################################################################
# Data Chuncks
####################################################################################
def data_chuncks(file_path, columns, memory_limitation):
        """
        # file_path : dataset file_path for imdb_dataset.csv (datatype : String)
        # columns : the columns on which dataset needs to be sorted (datatype : list of strings)
        # memory_limitation : At each time how many records from the dataframe can be loaded (datatype : integer)
        # Load the 2000 chunck of data every time into Data Structure called List of Sublists which is named as "chuncks_2000"
        # NOTE : This data_chuncks function uses the records from imdb_dataset. Only 2000 records needs to be loaded at a
                # Time in order to process for sorting using merge sort algorithm. After sorting 2000 records immediately
                # Store those 2000 sorted records into Floder named Individual by following Naming pattern given below.
        #Store all the output files in Folder named "Individual".
        #Output csv files must be named in the format Sorted_1, Sorted_2,...., Sorted_93
        #The below Syntax will help you to store the sorted files :
                    # name_of_csv = "Individual/Sorted_" + str(i + 1)
                    # sorted_df.reset_index(drop=True).to_csv(name_of_csv, index=False)

        # ***NOTE : Every output csv file must have 2000 sorted records except for the last ouput csv file which
                    might have less than 2000 records.

        Description:
        This code reads a CSV file, separates the data into chunks of data defined by the memory_limitation parameter,
        sorts each chunk of data by the specified columns using the merge_sort algorithm, and saves each sorted chunk
        as a separate CSV file. The chunk sets are determined by the number of rows in the file divided by the
        memory_limitation. The names of the sorted files are stored as "Individual/Sorted_" followed by a number
        starting from 1.
        """
        df = pd.read_csv(file_path)
        
        column_vals = [0]
        cols=['tconst']
        for column in columns:
            if(column == 'tconst'):
                continue
            index = column_names.index(column)
            column_vals.append(index)
            cols.append(column)
        
        total_chunks = len(df) // memory_limitation
        for i in range(0,total_chunks + 1):
            initial = i * memory_limitation
            final = min((i + 1) * memory_limitation, len(df))
            chunk = df.iloc[initial:final]
            chuncks_2000=FixedSizeList(2000)
            for j in range(0,len(chunk)):
                row=chunk.iloc[j]
                sublist = []
                for col in column_vals:
                    sublist.append(row[col])
                chuncks_2000.append(sublist)
            
            chuncks_2000 = merge_sort(chuncks_2000, column_vals)
            sorted_f=pd.DataFrame(chuncks_2000, columns=cols)
            name_of_csv = "Individual/Sorted_" + str(i + 1) + ".csv"
            sorted_f.reset_index(drop=True).to_csv(name_of_csv, index=False)


        #Write code for Extracting only 2000 records at a time from imdb_dataset.csv

        #Passing the 2000 Extracted Records and Columns indices for sorting the data
        #column_indxes are Extracted from the imdb_dataset indices by mapping the columns need to sort on which are
        #passed from the testcases.
        # arr=merge_sort(arr,column_indxes)

def f_merge(left, right, columns):

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if is_true(left[i], right[j], columns):
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def f_merge_sort(data, columns):

    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = f_merge_sort(data[:mid], columns)
    right = f_merge_sort(data[mid:], columns)

    return f_merge(left, right, columns)

def is_true(d1, d2, cols):
    r1= d1[0]
    r2= d2[0]
    for i in range(1,len(cols)):
        if type(r1[i]) == str and type(r2[i]) == str:
            if r1[i].strip() > r2[i].strip():
                return True
            elif r1[i].strip() < r2[i].strip():
                return False
        else:
            if r1[i] > r2[i]:
                return True
            elif r1[i] < r2[i]:
                return False
    return False

#Enable only one Function each from data_chuncks and Mystery_Function at a time

#Test Case 13
# data_chuncks('imdb_dataset.csv', ['startYear'], 2000)

#Test Case 14
data_chuncks('imdb_dataset.csv', ['primaryTitle'], 2000)

#Test Case 15
# data_chuncks('imdb_dataset.csv', ['tconst','startYear','runtimeMinutes' ,'primaryTitle'], 2000)


#Test Case 13
# Mystery_Function("Individual", 2000, ['tconst','startYear','runtimeMinutes' ,'primaryTitle'])
# Mystery_Function("Individual", 2000, ['startYear'])

#Test Case 14
Mystery_Function("Individual", 2000, ['primaryTitle'])

#Test Case 15
#Mystery_Function(file_path="Individual", 2000, ['startYear','runtimeMinutes' ,'primaryTitle'])