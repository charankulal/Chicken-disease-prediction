from ChickenDiseaseClassifier.constants import *
from ChickenDiseaseClassifier.entity.config_entity import DataIngestionConfig
from ChickenDiseaseClassifier.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(Path("D:\\PROJECTS\\Chicken Disease Prediction\\config\\config.yaml"))
        self.params = read_yaml(Path("D:\\PROJECTS\\Chicken Disease Prediction\\params.yaml"))

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config