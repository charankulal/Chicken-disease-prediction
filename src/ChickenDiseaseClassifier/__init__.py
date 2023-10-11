import os
import sys
import logging


# Specifying the log format
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#Specifying the directory
log_dir="logs"

# Specifying the path and filename and creating a new directory if doesn't exists
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

# Logging configuration

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers={
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    }
)

logger=logging.getLogger("ChickenDiseaseClassifierLogger")