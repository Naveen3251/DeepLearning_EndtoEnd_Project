#update the components
import urllib.request as request
from CNNClassifier.entity.config_entity import PrepareCallbacksConfig
import tensorflow as tf
import time
import os 
from pathlib import Path

class PrepareCallback:
    def __init__(self,config: PrepareCallbacksConfig):
        self.config=config

    @property
    def _create_tb_callbacks(self):
        timestamp=time.strftime('%Y-%m-%d-%H-%M-%S')

        tb_running_log_dir=os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at{timestamp}"
        )

        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath.as_posix(),
            save_best_only=True
        )
    
    #to get the above two methods
    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]