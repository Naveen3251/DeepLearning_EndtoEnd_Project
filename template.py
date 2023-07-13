import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] : %(message)s:')

project_name='CNNClassifier'

#list of folders have to create
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    #actually windows uses \ here i mentioned / so it autmatically handles
    filepath=Path(filepath)

    #seperating folder and file name
    #example:
    #file dir==>src\{project_name}\components
    #file==>__init.py__
    filedir,filename=os.path.split(filepath)

    #creating directory
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    #creating files if files not exsists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            logging.info(f"Creating empty file: {filepath}")
    #if files already existing
    else:
        logging.info(f"{filename} is already exists")