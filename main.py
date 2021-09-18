#importing transforms.py which is in the same directory and has the functions that we need
from transforms import *
from datetime import datetime

# Main
if __name__ == '__main__':
    #Starting program
    log_events("Starting program...")                                   #log_events function is defined in transforms.py

    #defining variable and empty data structures
    read_folder = "C:\\Chandu\\Projects\\AE\\"
    write_folder = "C:\\Chandu\\Projects\\AE\\output\\"
    source_file = "Transaction.csv"
    clean_data = []

    #Reading source data
    source_data = read_soruce_file(read_folder + source_file,",")
    log_events("Source file read successfully.")

    # Adding two new columns (Hash_Key and Request_Implementation_Days_Diff)
    # at the beginning and storing header for later use
    header = ["Hash_Key","Request_Implementation_Days_Diff"] + source_data[0]

    #Filter out the questionable data
    log_events("Filtering out the questionable data...")

    for i in range(len(source_data)):                                 #Traversing through the data to filter out the questionable data
        if (i != 0):  # and i < 10                                    #Skipping header. Also the follwing 3 columns are being read as string so letting them be and using string operations to filter out questionable data.
            if (    source_data[i][0].find(".") == -1                 #Filtering out rows where Account_ID has dot in them.
                    and source_data[i][3] in ("0", "1")               #Filtering out rows where Active Indicator is anything other than 0 or 1
                    and source_data[i][8] in ("PAID", "DISP", "REVR") #Filtering out rows where Account status is anything other than "PAID", "DISP", "REVR"
                ):
                source_data[i][10] = float(source_data[i][10])                  #keeping this numeric to sort later
                source_data[i].insert(0, create_hash(source_data[i][0]))        #Augmenting clean data with a md5 hash key at the beginning.
                source_data[i].insert(1,(datetime.strptime(source_data[i][3], '%d/%m/%Y %H:%M')
                                          - datetime.strptime(source_data[i][8], '%d/%m/%Y %H:%M')
                                        ).days
                                      ) #Calculating the response time in days and storing in new column


                # Storing clean records in new data structure as we process the data
                clean_data.append(source_data[i])

    #Out of for loop: clean data is ready
    log_events("Clean data is ready...")

    #Now understand the sort order by grouping post codes and finding average response times
    sort_order_df = find_best_response_post_code(header, clean_data)

    #Organize data in required sort order for final extraction
    final_df = organize_data_for_extracts(header,clean_data,sort_order_df)

    #Write final data to extracts
    extract_reports(write_folder,",",final_df)
    log_events("Report file extracted successfully.")

