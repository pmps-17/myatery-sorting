import csv
import time
import json
import pandas as pd

"""
Note : For test cases 7-10, you need to extract the required data (filter on conditions mentioned above)
and rename it to appropriate name as mentioned in the test case descriptions. You need to write the code
to perform this extraction and renaming, at the start of the skeleton file.
"""

column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']


#############################################################################################################
# Data Filtering
#############################################################################################################
def data_filtering(filelocation, num):
    """
    Data Filtering is for the test cases from 7 to 10.
    filelocation: imdb_dataset.csv location
    num: if num == 1 -> filter data based on years (years in range 1941 to 1955)
         if num == 2 -> filter data based on genres (genres are either ‘Adventure’ or ‘Drama’)
         if num == 3 -> filter data based on primaryProfession (if primaryProfession column contains substrings
                        {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
         if num == 4 -> filter data based on primary Names which start with vowel character.

    """
    # df = # Load the imdb_dataset.csv dataset 
    df = pd.read_csv(filelocation)
    if(num==1):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on years (years in range 1941 to 1955)
        #    df_year = #Store your filtered dataframe here
        df_year = df[(df['startYear'] >= 1941) & (df['startYear'] <= 1955)]
        df_year.reset_index(drop=True).to_csv("imdb_years_df.csv", index=False)

    if(num==2):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on genres (genres are either ‘Adventure’ or ‘Drama’)
        df_genres = df[(df['genres'] == 'Adventure') | (df['genres'] == 'Drama')]
        df_genres.reset_index(drop=True).to_csv("imdb_genres_df.csv", index=False)
    if(num==3):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on primaryProfession (if primaryProfession column contains
        #substrings {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
        #substrings = ['assistant_director', 'casting_director', 'art_director','cinematographer' ]
        df_professions = df[(df['primaryProfession'].str.contains('assistant_director', na=False)) | (df['primaryProfession'].str.contains('casting_director', na=False)) | (df['primaryProfession'].str.contains('art_director', na=False)) | (df['primaryProfession'].str.contains('cinematographer', na=False))]
        df_professions.reset_index(drop=True).to_csv("imdb_professions_df.csv", index=False)
    if(num==4):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on primary Names which start with vowel character.
        df_vowels = df[(df['primaryName'].str.upper().str.startswith('A').values) | (df['primaryName'].str.upper().str.startswith('E').values) | (df['primaryName'].str.upper().str.startswith('I').values) | (df['primaryName'].str.upper().str.startswith('O').values) | (df['primaryName'].str.upper().str.startswith('U').values) ]
        df_vowels.reset_index(drop=True).to_csv("imdb_vowel_names_df.csv", index=False)


#############################################################################################################
#Quick Sort
#############################################################################################################
def pivot_element(arr):
    #CODE For identifiying the pivot element
    pivot = (len(arr)//2) 
    return pivot
def quicksort(arr, columns):
    """
    The function performs the QuickSort algorithm on a 2D array (list of lists), where
    the sorting is based on specific columns of the 2D array. The function takes two parameters:

    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on

    The function first checks if the length of the input array is less than or equal to 1,
    in which case it returns the array as is. Otherwise, it selects the middle element of
    the array as the pivot, and splits the array into three parts: left, middle, right.

    Finally, the function calls itself recursively on the left and right sub-arrays, concatenates
    the result of the recursive calls with the middle sub-array, and returns the final sorted 2D array.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[pivot_element(arr)]
        left = []
        middle = []
        right = []
        for row in arr:
            if is_true(pivot, row, columns):
                left.append(row)
            elif is_true(row, pivot, columns):
                    right.append(row)
            else:
                middle.append(row)
        left = quicksort(left, columns)
        right = quicksort(right, columns)
        arr = left + middle + right
 
    #NEED TO CODE
    #Implement Quick Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.


#############################################################################################################
#Selection Sort
#############################################################################################################
def selection_sort(arr, columns):
    """
    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, returns the final sorted 2D array.
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if is_true(arr[min_idx], arr[j], columns):
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    #NEED TO CODE
    #Implement Selection Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Heap Sort
#############################################################################################################
def build_max_heap(arr, n, i, columns):
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i, columns)
        
def max_heapify(arr, n, i, columns):
    """
    arr: The input array to be transformed into a max heap
    n: The number of elements in the array
    i: The current index in the array being processed
    columns: The columns to be used for comparison

    The build_max_heap function is used to construct a max heap
    from an input array.
    """
    largest = i 
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n and is_true(arr[left], arr[largest], columns):
        largest = left

    if right < n and is_true(arr[right], arr[largest], columns):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest, columns)
    #NEED TO CODE
    #Implement heapify algorithm here


def heap_sort(arr, columns):
    """
    # arr: list of sublists which consists of records from the dataset in every sublists.
    # columns: store the column indices from the dataframe.
    Finally, returns the final sorted 2D array.
    """
    n = len(arr)
    build_max_heap(arr,n,n//2-1,columns)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0, columns)
    #NEED TO CODE
    #Implement Heap Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Shell Sort
#############################################################################################################
def shell_sort(arr, columns):
    """
    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, returns the final sorted 2D array.
    """
    n = len(arr)
    gaps = [n // 2]
    while gaps[-1] > 1:
        gaps.append(gaps[-1] // 2)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and is_true(arr[j - gap], temp, columns):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    #NEED TO CODE
    #Implement Shell Sort Algorithm
    #return Sorted array
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Merge Sort
#############################################################################################################
def merge(left, right, columns):
    """
    left: a list of lists representing the left sub-array to be merged
    right: a list of lists representing the right sub-array to be merged
    columns: a list of integers representing the columns to sort the 2D array on

    Finally, after one of the sub-arrays is fully merged, the function extends the result
    with the remaining elements of the other sub-array and returns the result as the final
    sorted 2D array.
    """

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
    #NEED TO CODE
    #Implement merge Logic
    #return Sorted array

def merge_sort(data, columns):
    """
    data: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, the function returns the result of the merge operation as the final sorted 2D array.
    """
    #NEED TO CODE
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid], columns)
    right = merge_sort(data[mid:], columns)
    #Mid value
    #Need to Code
    #Implement Merge Sort Algorithm
    #return Sorted array
    return merge(left, right, columns)
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Insertion Sort
#############################################################################################################
def insertion_sort(arr, columns):
    """
    # arr: list of sublists which consists of records from the dataset in every sublists.
    # columns: store the column indices from the dataframe.
    Finally, returns the final sorted 2D array.
    """
    for i in range(1, len(arr)):
        j = i 
        while j > 0 and is_true(arr[j-1], arr[j], columns):
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1
    #NEED TO CODE
    #Insertion Sort Implementation
    #Return : List of tconst values which are obtained after sorting the dataset.
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.
    

def is_true(r1, r2, cols):
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
    

#############################################################################################################
# Sorting Algorithms Function Calls
#############################################################################################################
def sorting_algorithms(file_path, columns, select):
    """
    # file_path: a string representing the path to the CSV file
    # columns: a list of strings representing the columns to sort the 2D array on
    # select: an integer representing the sorting algorithm to be used

    # colum_vals: is a list of integers representing the indices of the specified columns to be sorted.

    # data: is a 2D array of values representing the contents of the CSV file, with each row in
    the array corresponding to a row in the CSV file and each element in a row corresponding to a value
    in a specific column.

    More Detailed Description:

    df= #read imdb_dataset.csv data set using pandas library

    column_vals = #convert the columns strings passed from the test cases in the form of indices according to
                  #the imdb_dataset indices for example tconst column is in the index 0. Apart from the testcase
                  #Columns provided you must also include 0 column in the first place of list in column_vals
                  #for example if you have provided with columns {'startYear', 'primaryTitle'} which are in the
                  #indices {3,1}. So the column_vals should look like [0,3,1].

    data = #convert the dataframes into list of sublists, each sublist consists of values corresponds to
           #the particular columns which are passed from the test cases. In addition to these columns, each
           #sublist should consist of tconst values which are used to identify each column uniquely.
           #At the end of sorting all the rows in the dataset by using any algorithm you need to
           #Return : List of tconst strings which are obtained after sorting the dataset.
           #Example data looks like [['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #................so on ]
                                    # NOTE : tconst string value must be in first position of every sublist and
                                    # the other provided column values with respect to columns from the provided
                                    # test cases must be after the tconst value in every sublist. Every sublist
                                    # Represents one record or row from the imdb_dataset.csv (sublist of values).
    """
    #NEED TO CODE
    #Read imdb_dataset.csv
    #write code here Inorder to read imdb_dataset
    # df= #read imdb_dataset.csv data set using pandas library
    df = pd.read_csv(file_path)
    
    column_vals = [0]
    for column in columns:
        if(column == 'tconst'):
            continue
        index = column_names.index(column)
        column_vals.append(index)
    data=[]
    for i in range(0,len(df)):
        row=df.iloc[i]
        sublist = []
        for col in column_vals:
            sublist.append(row[col])
        data.append(sublist)
    #convert the dataframes into list of sublists, each sublist consists of values corresponds to
           #the particular columns which are passed from the test cases. In addition to these columns, each
           #sublist should consist of tconst values which are used to identify each column uniquely.
           #At the end of sorting all the rows in the dataset by using any algorithm you need to
           #Return : List of tconst strings which are obtained after sorting the dataset.
           #Example data looks like [['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #['tconst string 1', 'startYear value 1', 'primaryTitle String 1'],
                                    #................so on ]
                                    # NOTE : tconst string value must be in first position of every sublist and
                                    # the other provided column values with respect to columns from the provided
                                    # test cases must be after the tconst value in every sublist. Every sublist
                                    # Represents one record or row from the imdb_dataset.csv (sublist of values).

#############################################################################################################
# Donot Modify Below Code
#############################################################################################################
    if(select==1):
        start_time = time.time()
        output_list = insertion_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==2):
        start_time = time.time()
        output_list = selection_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==3):
        start_time = time.time()
        output_list = quicksort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==4):
        start_time = time.time()
        output_list = heap_sort(data, column_vals) #TODO:check
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==5):
        start_time = time.time()
        output_list = shell_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==6):
        start_time = time.time()
        output_list = merge_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    
   