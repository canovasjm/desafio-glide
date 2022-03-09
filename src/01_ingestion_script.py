#!/home/jm/anaconda3/bin/python

# required libraries
import os
import pandas as pd

from sqlalchemy import create_engine

# create db connection
#engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

def load_csv_sequentially(input_files_path):

    input_files_path_ = input_files_path
    
    # create a list of files to be loaded
    all_files = os.listdir(input_files_path_)    
    csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))
    csv_files.sort()

    # list of files in the source folder
    print(f"List of files to be processed: {csv_files}")
    
    # loop
    for i in range(len(csv_files)):
        print(f"Processing file: {csv_files[i]}")
        
        df_temp = pd.read_csv(input_files_path_ + "/" + f"{csv_files[i]}")
        print(df_temp.head(1))
        
        #df_temp.to_sql(name=table_name, con=engine, if_exists='append')

# main
def main():
    load_csv_sequentially(input_files_path="../data/raw/employee_data/")



if __name__ == "__main__":
    main() 
