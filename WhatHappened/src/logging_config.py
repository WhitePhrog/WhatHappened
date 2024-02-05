import os
import logging
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
log_folder_path = r"C:\Users\Octávio\Desktop\WhatHappened\WhatHappened\logs"

if not os.path.exists(log_folder_path):
    os.makedirs(log_folder_path)

current_datetime = datetime.datetime.now()
log_file_name = f'app_{current_datetime.strftime("%Y-%m-%d_%H-%M-%S")}.log'
log_file_path = os.path.join(log_folder_path, log_file_name)

file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)