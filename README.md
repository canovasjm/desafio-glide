# glide

## Set up  

First, clone the repository: 

`git clone https://github.com/canovasjm/desafio-glide.git`

I recommend to recreate the environment from the `environment.yml` file. If you are using [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) type:

`conda env create -n de --file environment.yml`

To activate the environment type:

`conda activate de`

## What you will find here

### :open_file_folder: `data`

A folder where the data (both raw and processed) is meant to be stored.  

### :open_file_folder: `exercise_directions`

File with directions and data sources for the project as provided in the initial `zip` file.  

### :open_file_folder: `notebooks`

Jupyter notebook with PySpark code.  

### :open_file_folder: `src`

Python script to ingest the raw data to a database.   

## Future work   

- Work with parquet format instead of CSV. This will require to transform input CSV files to parquet and to save data after transformations in parquet format  

- Based on the code snippets in presented in the Jupyter notebook, create a python script similar to the `01_ingestion_script.py` located under `src/` . This way, it will be possible to run the script on schedule, for example, using cron or an Airflow DAG

- Model the case when an employee joins/leaves the company more than once. For example:  

| snapshot_date   | employee_number   |  status |
|-----------------|:-----------------:|--------:|
| 2020-01-01      |    1              | Active  |
| 2020-01-02      |    1              | Inactive |
| ...             |   ...             | ...     |
| 2020-05-12      |    1              | Active   |
    

## Miscellaneous  

I tried to follow as much as possible this guidance for the repo structure: https://towardsdatascience.com/manage-your-data-science-project-structure-in-early-stage-95f91d4d0600

## Notes for my future self

Copy files from remote to local using `scp` and an identity file:  

```bash
scp -i /home/jm/.ssh/gcp -r canovasjm@34.136.25.197:/home/canovasjm/notebooks/glide /home/jm/Documents/repos/desafio-glide
```