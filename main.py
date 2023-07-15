from src.CNNClassifier import logger
from src.CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


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
