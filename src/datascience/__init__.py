#here we will set up login
import os
import sys
import logging

#asctime for time, levelname for info/ warning, module for in which module execution going on, message which msg i want to display     
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


log_dir="logs" #logs is folder where logging details wil b saved
log_filepath=os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

#prerequisit
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) #this required bcoz in terminal it will help to show msg of log_filepath
    ]

)

logger=logging.getLogger("datasciencelogger")