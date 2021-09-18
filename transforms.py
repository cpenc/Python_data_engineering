import csv
import hashlib
import pandas as pd
import numpy as np

#Function: log_events: Just printing whatever is being passed
def log_events(name):
    print(f'Logging event:  {name}')

'''
    Function: read_soruce_file 
    Reading file that is being passed and returning a 2D list
    Using try and except to catch any errors while reading the file.
    Terminating the program on unexpected errors
'''
def read_soruce_file(file_path,delimiter):
    try:
        with open(file_path, 'r') as sourceFile:
            source_data = list(csv.reader(sourceFile, delimiter=delimiter))
        return source_data
    except:
        log_events("**Error** reading source file.")
        log_events("**Error** terminating program...")
        exit(1)

'''
    Function: create_hash 
    Creating md5 hash for Account_ID column for clean data
'''
def create_hash(value):
    return hashlib.md5(value.encode("utf8")).hexdigest()

'''
    Function: find_best_response_post_code 
    There are several different response timeframs within a single post code based on
    'Implemented Date' and 'Request Date'. So this function take a average of all responses
    within a post code and then ranks all the post codes based on the mean reponse time.
    This ranking can later be used to sort data with earliest response first.
'''
def find_best_response_post_code(header, clean_df):
    try:
        df = pd.DataFrame(clean_df)
        df.columns = header

        #creating a new dataframe with only 2 columns
        df1 = df[['Request_Implementation_Days_Diff','Post Code ']].copy()

        #creating a new dataframe grouped at post code level and with their average response times
        return_df = df1.groupby("Post Code ")\
                    .mean()\
                    .reset_index()\
                    .rename(columns={'Request_Implementation_Days_Diff': 'Response_rank'})
        return return_df
    except:
        log_events("**Error** in function find_best_response_post_code.")
        log_events("**Error** terminating program...")
        exit(1)

'''
    Function: organize_data_for_extracts
    Sorting data keeping post codes with response time ascending
    and within each postcode, keeping $ Amount descending
'''
def organize_data_for_extracts(header,clean_df,sorted_df):
    try:
        df1 = pd.DataFrame(clean_df)
        df1.columns = header

        df2= sorted_df

        #join clean data and the post code ranking data that is derived based on
        # implmentation response time to organize data for final report extraction
        result = df1.merge(df2, on='Post Code ')

        #sort data
        result = result.sort_values(["Response_rank", "$ Amount "], ascending = (True, False))

        #selecting only those columns that we need
        result = result[['Hash_Key', 'Account_ID ', 'CODE ',
           'Implemented Date ', 'Active Indicator ', 'Account Type ', 'Service ',
           'BU', 'Request Date ', 'Account status ', 'Status Code ', '$ Amount ',
           'Version ', 'Agent ID ', 'FIBRE ', 'last Updated Date ',
           'Property TYPE ', 'Post Code ']]

        return result
    except:
        log_events("**Error** in function organize_data_for_extracts.")
        log_events("**Error** terminating program...")
        exit(1)

'''
    Function: extract_reports 
    Extracting final data into json files
    Using try and except to catch any errors while extracting the files.
    Terminating the program on unexpected errors
'''
def extract_reports(file_path,delimiter,data):
    try:
        df = pd.DataFrame(data)
        for i, delta in df.groupby(np.arange(len(df))//1000):
            delta.to_json(file_path+f'extract_{i}.json', orient='columns', index = 'false')
        return 0
    except:
        log_events("**Error** extracting report files.")
        log_events("**Error** terminating program...")
        exit(1)
