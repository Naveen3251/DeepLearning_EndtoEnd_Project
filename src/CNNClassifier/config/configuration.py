from src.CNNClassifier.constants import *
from src.CNNClassifier.utils.common import read_yaml,create_directories
from src.CNNClassifier.entity.config_entity import DataIngestionConfig
# Update configuration manager
class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    # Data ingestion function
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        # Return type of function
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir  # Update the argument name here
        )
        
        return data_ingestion_config