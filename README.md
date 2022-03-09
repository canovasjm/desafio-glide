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

## Miscellaneous  

I tried to follow as much as possible this guidance for the repo structure: https://towardsdatascience.com/manage-your-data-science-project-structure-in-early-stage-95f91d4d0600

## Notes for my future self

Copy files from remote to local using `scp` and an identity file:  

```bash
scp -i /home/jm/.ssh/gcp -r canovasjm@34.136.25.197:/home/canovasjm/notebooks/glide /home/jm/Documents/repos/desafio-glide
```