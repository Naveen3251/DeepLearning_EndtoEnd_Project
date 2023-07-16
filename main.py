from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


#for data 
STAGE_NAME="Data Ingestion stage"
try:
    #excution stage by stage
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completd <<<<<<<<<\n\nX=============X')
except Exception as e:
    logger.exception(e)
    raise e

#for training model
STAGE_NAME="Prepare base model"
try:
    #excution stage by stage
    logger.info(f"******************************************")
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    prepare_base_model=PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completd <<<<<<<<<\n\nX=============X')
except Exception as e:
    logger.exception(e)
    raise e