import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


project_name = "datascience"

list_of_files = [
    ".gthub/workflows/.gitkeep",
    #__init__.py files are used to mark directories on disk as Python package directories, they are constructors of the package
    f"src/{project_name}/__init__.py", # creates __init__.py in src folder as package, it is constructed later in the project
    f"src/{project_name}/components/__init__.py", #constructs components folder #components is for different components of the project
    f"src/{project_name}/utils/__init__.py", #constructs utils folder #utils is for generic functions accross the project
    f"src/{project_name}/utils/common.py", #common to most of different components of the project
    f"src/{project_name}/config/__init__.py", #constructs config folder #config is for configuration files
    f"src/{project_name}/config/configuration.py", #configuration file for the project
    f"src/{project_name}/pipeline/__init__.py", #constructs pipeline folder #pipeline is for different pipelines of the project
    f"src/{project_name}/entity/__init__.py", #constructs entries folder #entries is for different entry points of the project
    f"src/{project_name}/entity/config_entity.py", #configuration entity for the project
    f"src/{project_name}/constants/__init__.py", #constructs constants folder #constants is for different constants of the project
    #reason for creating yaml files is so we can read all configuration files in a single place
    "config/config.yaml", #configuration file for the project, it has different parameters for the project
    "params.yaml", #parameters file for the project
    "schema.yaml", #schema file for the project
    "main.py", #main file for the project
    "Dockerfile", #Dockerfile for the project
    "requirements.txt", #requirements file for the project
    "setup.py", #it helps to create entire project as a package
    "research/research.ipynb", #research file for the project
    "templates/index.html" #template file for the project
    
]

#to create the files and directories
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass #its for not creating any content in the file, just creating the file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exits")

