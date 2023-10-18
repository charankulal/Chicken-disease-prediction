from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.components.prepare_base_model import PrepareBaseModel
from ChickenDiseaseClassifier.config.configuration import ConfigurationManager

STAGE_NAME="Preparing Base Model Stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        prepare_base_model_config=config.get_prepare_base_model_config()
        prepare_base_model=PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        
if __name__ == '__main':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed<<<<\n\nx==============x")
        
    except Exception as e:
        logger.exception(e)
        raise e