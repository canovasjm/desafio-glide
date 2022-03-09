#!/home/jm/anaconda3/bin/python

# How to run:
# python 01_ingestion_script.py --input_path ../data/raw/employee_data/

# required libraries
import os
import argparse

import pandas as pd

from sqlalchemy import create_engine

# create db connection
#engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

# function to load one CSV at a time
def load_csv_sequentially(input_path):
    '''
    Looks for CSVs in the input_path , stores these files names in a list, and iterates through its elements
    reading the CSV in a Pandas df and sending it to the DB
    '''
    # create a list of files to be loaded
    all_files = os.listdir(input_path)    
    csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))
    csv_files.sort()

    # list of files in the source folder
    print(f"List of files to be processed: {csv_files}")
    
    # loop
    for i in range(len(csv_files)):
        print(f"Processing file: {csv_files[i]}")
        
        df_temp = pd.read_csv(input_path + "/" + f"{csv_files[i]}")
        print(df_temp.head(1))
        
        #df_temp.to_sql(name=table_name, con=engine, if_exists='append')

# main
def main(params):
    input_path = params.input_path #"../data/raw/employee_data/"
    load_csv_sequentially(input_path)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    parser.add_argument('--input_path', required=True, help='path where the CSV to ingest are located')
    
    args = parser.parse_args()

    main(args) 
