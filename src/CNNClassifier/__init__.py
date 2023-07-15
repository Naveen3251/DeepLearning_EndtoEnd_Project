import os
import sys
import logging

#logging string
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#log directory and file
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)


#final log
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)#printing the log in the terminal
    ]
)

logger=logging.getLogger("CNNClassifierLogger")