from CNNClassifier.config.configuration  import ConfigurationManager
from CNNClassifier.components.evaluation import Evaluation
from CNNClassifier import logger

STAGE_NAME="Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        val_config=config.get_validation_config()
        evaluation=Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__=='__main__':
    try:
        logger.info(f"*************************")
        logger.info(f">>>>>>>>>>>stage {STAGE_NAME} started<<<<<<<<<<<<")

        obj=EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>stage {STAGE_NAME} ended<<<<<<<<<<<<\n\nx+++++++++++++++++x")
    except Exception as e:
        logger.exception(e)
        raise e

