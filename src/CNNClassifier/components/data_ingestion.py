#update components
import os
import urllib.request as request # to download the data
import zipfile #unzip the file
from src.CNNClassifier import logger #custom logger
from src.CNNClassifier.utils.common import get_size #to se the data soze
from src.CNNClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

# Update DataIngestion class
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    # Download the file from GitHub
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! Info: {headers}")
        else:
            logger.info(f"File already exists of size: {os.path.getsize(self.config.local_data_file)}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)