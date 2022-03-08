#!/home/jm/anaconda3/bin/python

# required libraries
import os
import pandas as pd

from sqlalchemy import create_engine

# load files
all_files = os.listdir("./employee_data/")    
csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))
csv_files.sort()

# list of files in the source folder
print(f"List of files to be processed: {csv_files}")

#engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

# loop
for i in range(len(csv_files)):
    print(f"Processing file: {csv_files[i]}")
    
    df_temp = pd.read_csv(f"./employee_data/{csv_files[i]}")
    print(df_temp.head(1))
    
    #df_temp.to_sql(name=table_name, con=engine, if_exists='append')
