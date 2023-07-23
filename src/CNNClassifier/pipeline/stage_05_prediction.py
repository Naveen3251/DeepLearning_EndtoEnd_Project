from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import numpy as np
class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))  # Update target_size here
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        print(test_image)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return [{"image": prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{"image": prediction}]
