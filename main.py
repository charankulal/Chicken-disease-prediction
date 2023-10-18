from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ChickenDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed<<<<\n\nx==============x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Preparing Base Model Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed<<<<\n\nx==============x")
        
except Exception as e:
    logger.exception(e)
    raise e